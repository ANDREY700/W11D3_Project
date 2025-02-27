# ELBRUSE Bootcamp 
# 13-02-2025
# Week 9 Day 4 Project
# team: Dasha, Alina, Ilya, Andrey u

import streamlit as st
import pandas as pd



#initialization ----------------------------


#Основная страница  ----------------------------
# боковая панель
page01 = st.Page("pages/page_01.py", title = 'Оглавление:')

page02 = st.Page("pages/page_02.py", title = 'Описание Проекта')
page03 = st.Page("pages/page_03.py", title = '-> Умный поиск книг')
page04 = st.Page("pages/page_031.py", title = 'Описание моделей')


pg = st.navigation([page01,  page02, 
                    page03, page04
                    ], expanded=True)
pg.run()


st.sidebar.title('Команда проекта:')
st.sidebar.write('Галина Горяинова')
st.sidebar.write('Анатолий Яковлев')
st.sidebar.write('Андрей Абрамов')

    


    






