



# очистка файла all_books.csv

import pandas as pd
import re
import nltk
from tqdm import tqdm 
from nltk.stem.snowball import SnowballStemmer # lemmatization
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer # vectorization



base_path = 'U:/01 Elbrus Bootcamp/56 W11D3 Parsing/Project'
all_books_file = '/data/all_books.csv'
book_anno_BOW = '/data/books_BOW.csv'
book_anno_BOW_clean = '/data/books_BOW_clean.csv'


all_books = pd.read_csv(base_path + all_books_file, index_col=0)

all_books.head()
all_books.loc[0, :]
# len(all_books)
all_books.shape

# clean the content -> only chars =======================================
for i in range(0, len(all_books)):
    all_books.loc[i, 'annotation'] = re.sub('[^а-яА-Я ]', ' ', all_books.loc[i, 'annotation'])
    
all_books.head()


# tokenization -> split the text by tokens to list  =======================================
text_list = []
for i in tqdm(range(0, len(all_books))):
    text_list.append(nltk.word_tokenize(all_books.loc[i, 'annotation'], language='russian'))
text_list[:1] # -> ok

# lemmatization -> to the base of simple word =======================================
Snow = SnowballStemmer('russian')

for i in tqdm(range(0, len(text_list))):
    for j in range(0, len(text_list[i])):
        text_list[i][j] = Snow.stem(text_list[i][j])
text_list[:1] # -> ok 

# stop words removing =======================================
stop_words_russian = stopwords.words('russian')

text_list_cleaned = []
for i in tqdm(range(0, len(text_list))):
    a = []
    for j in range(0, len(text_list[i])):
        if text_list[i][j] not in stop_words_russian:
            a.append(text_list[i][j])
    text_list_cleaned.append(a)
text_list_cleaned[:1] # -> ok  

# vectorization =======================================
Vectorizer = CountVectorizer()
# connect separeted words to the string
text_list_cleaned3 = []
for i in range(0, len(text_list)):
    text_list_cleaned3.append(' '.join(text_list_cleaned[i]))
text_list_cleaned3[:2] # -> ok 

# Vectorization 1
# matrix_count = Vectorizer.fit_transform(text_list_cleaned3)
# matrix_count.shape

# print('Vocab:', Vectorizer.vocabulary_)
# print('names:', Vectorizer.get_feature_names_out())
# print('array:', matrix_count.toarray())


# Vectorization 2
tfidfvec = TfidfVectorizer(min_df=80, max_df=0.2)
vectorized_data = tfidfvec.fit_transform(text_list_cleaned3)

print(tfidfvec.get_feature_names_out())
len(tfidfvec.get_feature_names_out())
print(vectorized_data.toarray())

books_BOW = pd.DataFrame(vectorized_data.toarray(), columns=[*tfidfvec.get_feature_names_out()])
books_BOW.head()
books_BOW.to_csv(base_path + book_anno_BOW)


zero_len = len([*tfidfvec.get_feature_names_out()])
zero_list = [0]*zero_len
books_BOW_clean = pd.DataFrame([], columns=[*tfidfvec.get_feature_names_out()]).T
books_BOW_clean['0'] = zero_list
books_BOW_clean = books_BOW_clean.T
books_BOW_clean.head()
books_BOW_clean.to_csv(base_path + book_anno_BOW_clean)
