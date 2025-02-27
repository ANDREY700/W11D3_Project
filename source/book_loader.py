

# books loader
# Litres.ru
# 26-02-2025

# lybs
import pandas as pd
import re
import requests
from bs4 import BeautifulSoup
import tqdm
import random
import time


# что мы делаем сейчас? ----------------------------------
#  - скачиваем ссылки на книги
#  - или скачиваем описание самих книг
TO_DO = 'links'
#TO_DO = 'books'


# создаем все каталоги, файлы и пр ------------------------
base_path = 'U:/01 Elbrus Bootcamp/56 W11D3 Parsing/Project'
genre_list_file = '/data/genre_groups.csv'
book_links_list_file = '/data/book_links.csv'
books_file = '/data/books.csv'

#book_links_list = pd.DataFrame.from_dict({'Genre_name':[], 'Book_name':[], 'Book_link':[]})
#book_links_list.to_csv(base_path + book_links_list_file)

# header for requests
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) " 
           "AppleWebKit/537.36 (KHTML, like Gecko) "
           "Chrome/39.0.2171.95 Safari/537.36"
           }

pages_limit = 100

# load links to books -------------------------------------
if TO_DO == 'links':

    # загружаем массив жанров 
    genre_list = pd.read_csv(base_path + genre_list_file, index_col=0)
    #len(genre_list) # 56

    # загружаем файл с уже собранными ссылками на книги
    book_links_list = pd.read_csv(base_path + book_links_list_file, index_col=0)

    # собираем ссылки на книги с каждой страницы с интервалом 20 сек
    # 25 книг на странице
    # предположим из каждого раздела можно собрать по 100 книг, это пусть будет 15 страниц
    #i = 0
    for i in tqdm.tqdm(range(0, len(genre_list)), 'Genres: '):
        
        # новый жанр
        page_num = genre_list.loc[i, 'latest_page_number']
        total_pages = genre_list.loc[i, 'pages']
        # начнем со второй страницы - первую сложно обрабатывать :)
        # можно сделать массив открытых книг, но сначала попробуем по-быстрому
        if page_num == 0 :
            page_num = 2
        else:
            page_num +=  1
        if total_pages == 0 :
            total_pages = 1000                        
                
        while (page_num < pages_limit) & (page_num < total_pages):        
            page_ready = True # сбрасываем когда странийа сайта прочитана                    
            while page_ready:           
        
                new_link = 'https://www.litres.ru' + genre_list.iloc[i,1] + '?view=showroom&page=' + str(page_num)
                single_page = requests.get(new_link, headers=headers, timeout=60)
                
                # если все в порядке           
                if single_page.status_code == 200: # 
                    single_page_soup = BeautifulSoup(single_page.text, 'html.parser')
                    title = single_page_soup.find('div', class_='PaginatedContent_wrapper___IXwB').find('div', class_='PaginatedContent_content__HG6bS').find_all('a', tabindex='0')
                    # делаем массив строк
                    a1 = str(title).split(sep="</a>, ")
                    
                    # идем по строкам
                    new_book_links = {'Genre_name':[], 'Book_name':[], 'Book_link':[]}
                    # line=0
                    for line in range(0, len(a1)):   
                        if a1[line].find('aria-label') > 0:
                            a1_bs = BeautifulSoup(a1[line], 'html.parser')
                            name_link = a1_bs.find('a')['href'] 
                            name = a1_bs.find('a')['aria-label'] 
                            new_book_links['Book_name'].append(name)
                            new_book_links['Book_link'].append(name_link)
                            new_book_links['Genre_name'].append(genre_list.loc[i, 'Group'])
                    #len(new_book_links['Genre_name'])
                    book_links_list = pd.concat([book_links_list, pd.DataFrame.from_dict(new_book_links)], axis=0)
                                        
                    genre_list.loc[i, 'latest_page_number'] = page_num
                    page_num +=1
                    
                    if total_pages == 1000:
                        total_pages = single_page_soup.find('div', class_='PaginatedContent_paginator___2ugs').find_all('li', class_='Paginator_page___fg9G')
                        b1 = BeautifulSoup(str(total_pages).split(sep=",")[-1], 'html.parser').getText()
                        non_decimal = re.compile(r'[^\d.]+')
                        b1 = non_decimal.sub('', b1)
                        total_pages = int(b1)
                        genre_list.loc[i, 'pages'] = total_pages
                        genre_list.to_csv(base_path + genre_list_file)
                    
                    # пауза ~25 сек                    
                    time.sleep(random.randint(6, 10))                    
                    # end this page cycle
                    page_ready = False
                    
                else:
                    # пауза ~25 сек                    
                    time.sleep(random.randint(120, 300))                    
    
        # сохраняем в файл     
        #genre_list['latest_page_number'] = 0
        genre_list.to_csv(base_path + genre_list_file)    
        book_links_list.to_csv(base_path + book_links_list_file)        
        
    len(book_links_list)



# убираем дубликаты --------------------------
if TO_DO == 'dublicates':
    # загружаем файл с уже собранными ссылками на книги
    book_links_list = pd.read_csv(base_path + book_links_list_file, index_col=0)
    len(book_links_list)
    book_links_list.reset_index(drop=True)
    book_links_list = book_links_list.drop_duplicates(subset=['Book_name'])
    len(book_links_list)
    book_links_list.to_csv(base_path + book_links_list_file)
    



# собираем описание книг
if TO_DO == 'books':
    books = pd.read_csv(base_path + books_file, index_col=0)
    
    # загружаем файл с уже собранными ссылками на книги
    book_links_list = pd.read_csv(base_path + book_links_list_file, index_col=0)
    book_links_list = book_links_list.sort_values(by='Book_link', ascending=True)
    
    #for line in tqdm.tqdm(book_links_list):
    for line in tqdm.tqdm(range(0, len(book_links_list))):
        line = book_links_list.iloc[i, :]
    #line = book_links_list.iloc[0, :]
    #if True:               
        # проверить что такого фильма еще нет
        k = books[books['title'] == line.Book_name]
        if len(k) == 0:
            #
            page_ready = True # сбрасываем когда странийа сайта прочитана                    
            while page_ready:   
                
                book_link = 'https://www.litres.ru' + line.Book_link 
                book_page = requests.get(book_link, headers=headers, timeout=60) 
                
                # если все в порядке           
                if book_page.status_code == 200: 
                    new_book = {'page_url':[], 'image_url':[], 'author':[], 'title':[], 'annotation':[], 'book_image_file_name':[]}
                    
                    book_soup = BeautifulSoup(r.text, 'html.parser')
                    title = book_soup.find('body').find('div', id='layout-root').find('main', id='main').find('div', id='book-card__wrapper').find('h1', itemprop='name')                    
                    new_book['title'].append(title.getText())
                    new_book['page_url'].append(book_link)
                    new_book['book_image_file_name'].append('')
                    
                    author = book_soup.find('body').find('div', id='layout-root').find('main', id='main').find('div', class_='Truncate_truncated__jKdVt')
                    new_book['author'].append(author.getText())
                    
                    image_link = book_soup.find('body').find('div', id='layout-root').find('main', id='main').find('img', itemprop='image')['src']
                    new_book['image_url'].append(image_link)

                    # дополнительный запрос на раскрытие описания книги
                    headers3 = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) " 
                                "AppleWebKit/537.36 (KHTML, like Gecko) "
                                "Chrome/39.0.2171.95 Safari/537.36",
                                "Referer": "https://www.litres.ru/book/anne-dar/pobedonosec-71641255/"
                                }
                    url3 = "https://api.litres.ru/tracker/api/event/"
                    r3 = requests.get(url3, headers=headers3, timeout=60)
                    if r3.status_code == 200:
                        soup3 = BeautifulSoup(r3.text, 'html.parser')
                        content = soup3.find('body').find('div', id='layout-root').find('main', id='main').find('div', class_='BookCard_book__content__7J8Fc').find('div', class_='BookCard_truncate__jrVwM')
                        book_content = content.getText() 
                        new_book['annotation'].append(book_content)
                    
                    books = pd.concat([books, pd.DataFrame.from_dict(new_book)], axis=0)
                    
                    # пауза ~10 сек
                    time.sleep(random.randint(6, 9))                    
                    # end this page cycle
                    page_ready = False
                    books.to_csv(base_path + books_file)
                else:
                    # пауза ~25 сек                    
                    time.sleep(random.randint(120, 180))                  
            #
        
            #





