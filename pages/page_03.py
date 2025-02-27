

import streamlit as st
import numpy as np
import pandas as pd
from pages.source.text_to_array import books_cosine_similarity, text_to_array

# tables


# models 

# local preparation

# title itself
col1, col2, col3 = st.columns(spec=[0.4, 0.5, 0.2])
with col1:
    st.image('images/book03.PNG', width=160)
with col2:
    st.subheader("Умный поиск книг")
    
st.divider()
st.subheader("1. Статус загрузки моделей: ")

all_books_file = 'data/all_books.csv'
book_anno_BOW_file = 'data/books_BOW.csv'
book_anno_BOW_clean_file = 'data/books_BOW_clean.csv'

try:
    book_anno_BOW_clean = pd.read_csv(book_anno_BOW_clean_file, index_col=0)
    book_anno_BOW_clean_loaded = True
    st.write('Файл books_BOW_clean.csv загружен')
except:
    book_anno_BOW_clean_loaded = False
    st.write('Сложности в загрузке файла books_BOW_clean.csv')
 
try:
    book_anno_BOW = pd.read_csv(book_anno_BOW_file, index_col=0)
    book_anno_BOW_loaded = True
    st.write('Файл books_BOW.csv загружен')
except:
    book_anno_BOW_loaded = False
    st.write('Сложности в загрузке файла books_BOW.csv')

try:
    all_books = pd.read_csv(all_books_file, index_col=0)
    all_books_loaded = True
    st.write('Файл all_books.csv загружен')
except:
    all_books_loaded = False
    st.write('Сложности в загрузке файла all_books.csv')




st.divider()

st.subheader("2. Пользовательский запрос: ")
text_pos = st.text_area('Поле для ввода желаемого описания книги', value='самый красивый японский поэт чувства лирика стихотворение')
#st.selectbox("Применить модели поиска", ["использовать все вместе", "Использовать по отдельности"])

answers_number = st.number_input("Число найденных книг на странице", 0, 100, value=5)

if (book_anno_BOW_clean_loaded & book_anno_BOW_loaded) & (all_books_loaded):
    if st.button('Найти'):
        if len(text_pos) >0 :
            st.divider()   
            st.subheader("Модель #1")
            #online_results_pos = models_apply(table=online_results, text=text_pos)
            st.subheader("Результат поиска книг по желаемому описанию:")
            t2 = text_to_array(text=text_pos, book_anno_BOW_clean=book_anno_BOW_clean)
            answer = books_cosine_similarity(BOW=book_anno_BOW, all_books=all_books, text_array=t2, top=answers_number).reset_index()
            for i in range(0,answers_number):
                col1, col2, col3 = st.columns(spec=[0.2, 0.7, 0.1])
                with col1:
                    st.image(answer.loc[i, 'image_url'], width=100)
                with col2:        
                    #,page_url,image_url,author,title,annotation,book_image_file_name            
                    st.write(answer.loc[i, 'author'])
                    st.write(answer.loc[i, 'title'])
                    st.write(answer.loc[i, 'annotation'])
                with col3:        
                    pass
                    st.write(f'{answer.loc[i, 'cosine']:.2f}') 
            st.divider()   
            #st.table(answer)
        else:
            st.write('Текст запроса не должен бюыть пустым!')
        
        
    

