
import pandas as pd

# all csv book files to single one

def three_to_one_scv(filename1:str, filename2:str, filename3:str=''):
    bookfile1_loaded, bookfile2_loaded, bookfile3_loaded = False, False, False   
    
    if filename1 != '':
        try :
            bookfile1 = pd.read_csv(filename1, index_col=0)
        except:
            print('- file-1 недоступен')
            bookfile1_loaded = False
        else:       
            print(f'Book file-1 size is {len(bookfile1)}')
            bookfile1_loaded = True
    
    if filename2 != '':
        try :
            bookfile2 = pd.read_csv(filename2, index_col=0)
        except:
            print('- file-2 недоступен')
            bookfile2_loaded = False
        else:       
            print(f'Book file-2 size is {len(bookfile2)}')
            bookfile2_loaded = True

    if filename3 != '':
        try :
            bookfile3 = pd.read_csv(filename3, index_col=0)
        except:
            print('- file-3 недоступен')
            bookfile3_loaded = False
        else:       
            print(f'Book file-3 size is {len(bookfile3)}')
            bookfile3_loaded = True

    
    if bookfile1_loaded & bookfile2_loaded:
        if bookfile1_loaded & bookfile2_loaded & bookfile3_loaded:
            bookfile = pd.concat([bookfile1, bookfile2, bookfile3])    
        else:
            bookfile = pd.concat([bookfile1, bookfile2])
    else:
        bookfile = []
    
    bookfile = bookfile.reset_index(drop=True)
    print(f'Result book file size is {len(bookfile)}')
    
    return bookfile


base_path = 'U:/01 Elbrus Bootcamp/56 W11D3 Parsing/Project'
all_books_file = '/data/all_books.csv'

books = three_to_one_scv(filename1=base_path+'/data/books.csv', 
                         filename2=base_path+'/data/books_chitai_gorod.csv', 
                         filename3='')

books.to_csv(base_path + all_books_file)   


