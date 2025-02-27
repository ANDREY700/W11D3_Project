# ELBRUSE Bootcamp 
# 13-02-2025
# Week 9 Day 4 Project
# team: Dasha, Alina, Ilya, Andrey 

import streamlit as st
import pandas as pd

image_size = 160

#st.header('Оглавление')

st.write('-------------------------------------------------------------------------------------')

col1, col2, col3 = st.columns(spec=[0.4, 0.3, 0.4])
with col1:
    st.page_link("pages/page_02.py", label='Описание проекта')
with col2:
    st.image('images/book04.jpg', width=image_size)

st.write('-------------------------------------------------------------------------------------')

col1, col2, col3 = st.columns(spec=[0.4, 0.3, 0.4])
with col2:
    st.image('images/book03.PNG', width=image_size)
with col3:
    st.page_link("pages/page_03.py", label='Умный поиск книг')


st.write('-------------------------------------------------------------------------------------')


col1, col2, col3 = st.columns(spec=[0.4, 0.3, 0.4])
with col1:
    st.page_link("pages/page_031.py", label='Описание моделей')
with col2:
    st.image('images/book06.jpg', width=image_size)

st.write('-------------------------------------------------------------------------------------')
