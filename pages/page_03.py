

import streamlit as st
import numpy as np
import pandas as pd
from hosp_feedback_folder.functions01 import *


model_path = "models/face_yolo11m.pt"
# models load !!!    

# local preparation
online_results = pd.DataFrame.from_dict({'Модель':['GaussianNB',
                                                   'LogisticRegression',
                                                   'SVC',
                                                   'AdaBoostClassifier',
                                                   'GradientBoostingClassifier',
                                                   'LinearRegression',
                                                   'ruBERT-tiny2',
                                                   'RNN with attantion'                                                   
                                                   ], 
                                                   'Ответ BOW':['-', '-','-','-','-','-','-','-',], 
                                                   'Ответ TFI-DF':['-', '-','-','-','-','-','-','-',], 
                                                   'Время, сек':['-', '-','-','-','-','-','-','-',]})

online_results_pos = online_results
online_results_neg = online_results

# title itself
st.title("Страница 1.")
st.header("1. Классификация отзывов на поликлиники")



st.divider()
st.write("Отзыв-1")
text_pos = st.text_area('Поле для ввода отзыва о поликлиннике: (добавлен позитивный пример)', value='Хороший врач. Хочу выразить позитив замечательному доктору - Ивановой Анне. Было очень сложно, сделала все отлично! большое вам спасибо!')
if  st.button('Оценить Отзыв-1'):
    online_results_pos = models_apply(table=online_results, text=text_pos)
    st.write("Оценка отзыва с использованием подготовленных моделей:")
   
    st.table(online_results_pos)
    
    st.write(models_apply2(text_pos))






st.divider()
st.write("Отзыв-2")
text_neg = st.text_area('Поле для ввода отзыва о поликлиннике: (добавлен негативный пример)', value='Плохой главный врач. Находясь на приеме у врача-стоматолога стала свидетелем вопиющего хамства. Зашел в кабинет врач, как узнала позже - Главный врач поликлиники (лицо не русской национальности) и стал по-хамски общаться с персоналом, грубить и затыкать им рот. Не стесняясь пациентов, коллег, хамил персоналу. Как такого недалекого человека можно ставить на руководящую должность?? Позорище!')
if st.button('Оценить Отзыв-2'):
    online_results_neg = models_apply(table=online_results, text=text_neg)
    st.write("Оценка отзыва с использованием подготовленных моделей:")
    st.table(online_results_neg)
