


# function of text preparation for streamlit project
# import os
# os.getcwd()
# os.chdir('U:/01 Elbrus Bootcamp/56 W11D3 Parsing/Project')

import pandas as pd
import numpy as np
import re
import nltk
from tqdm import tqdm 
from nltk.stem.snowball import SnowballStemmer # lemmatization
from nltk.corpus import stopwords
#from sklearn.metrics.pairwise import cosine_similarity



probe_text = 'самый красивый японский поэт чувства лирика стихотворение'



def text_to_array(book_anno_BOW_clean, text:str=''):
    # clean the content -> only chars =======================================
    text = re.sub('[^а-яА-Я ]', ' ', text)
    
    # tokenization -> split the text by tokens to list  =======================================
    text_list = []
    text_list.append(nltk.word_tokenize(text, language='russian'))
    
    # lemmatization -> to the base of simple word =======================================
    Snow = SnowballStemmer('russian')
    for j in range(0, len(*text_list)):
        text_list[0][j] = Snow.stem(text_list[0][j])
    
    # stop words removing =======================================
    stop_words_russian = stopwords.words('russian')
    text_list_cleaned = []
    for i in range(0, len(*text_list)):
        if text_list[0][i] not in stop_words_russian:
            text_list_cleaned.append(text_list[0][i])
            
    # preparinf an array on the text typed
    a = book_anno_BOW_clean.copy()
    a_columns = a.columns   
    text_list_cleaned = [item for item in text_list_cleaned if item in a_columns]
       
    for i in range(0, len(text_list_cleaned)):
        a.loc[0, text_list_cleaned[i]] += 1
            
    return a[a_columns]



#text = probe_text

#top=5
#text_array = m
def books_cosine_similarity(BOW, all_books, text_array:str, top:int=10):
    answer = []
    i=0
    for i in range(0, len(BOW)) :
        a = np.dot(np.array(BOW.loc[i, :].values), 
                   np.array(*text_array.values)) / (np.linalg.norm(BOW.loc[i, :].values) +0.001) * (np.linalg.norm(np.array(*text_array.values))+0.001)
        answer.append(a)                                                           
    b = all_books.copy()
    b['cosine'] = answer
    b = b.sort_values(by='cosine', ascending=False)
    return b.iloc[:top, :]



def test01():
    return '1000'



# m = text_to_array(probe_text)

# nn = books_cosine_similarity(m, 5)

# np.array(book_anno_BOW.iloc[i, 1:10])
#https://sky.pro/wiki/python/raschet-kosinusnogo-skhodstva-dvukh-spiskov-chisel-v-python/
# nums1 = np.array([1, 2, 3])
# nums2 = np.array([4, 5, 6])
# cosine_similarity = np.dot(nums1, nums2) / (np.linalg.norm(nums1) * np.linalg.norm(nums2)) 

