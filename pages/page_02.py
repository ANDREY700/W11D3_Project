
# ELBRUSE Bootcamp 
# 13-02-2025
# Week 9 Day 4 Project
# team: Dasha, Alina, Ilya, Andrey 


import streamlit as st
import pandas as pd


#st.title('Страница 01')
st.header('Умный поиск книг')
st.subheader('Описание Проекта')
st.write('Магазин электронных книг хочет усовершенствовать поиск. Сейчас поиск происходит по автору и названию книги, при этом никак не учитывается аннотация (а большая часть из них даже не добавлена на сайт). Вашей команде предстоит собрать выборку из не менее, чем 5000 аннотаций c сайта и построить систему поиска наиболее подходящих под пользовательский запрос книг.')

st.subheader('План проекта:')
st.write('Разработать систему поиска книги по пользовательскому запросу. Сервис должен принимать на вход описание книги от пользователя и возвращать заданное количество подходящих вариантов. Демо должно быть развернуто через streamlit. Макет интерфейса сервиса можно найти тут. Сервис должен быть развернут на huggingface spaces.')

st.subheader('Релизы:')
st.write('-------------------------------------------------------------------------------------')
st.write('Релиз 1.0')
st.write('Срок: среда, 17:00')
st.write('* сделать csv-файл следующей структуры:')
st.write('page_url,	image_url,	author,	title,	annotation')
st.write('* сделать py-файл, содержащий скрипт с парсингом и сохранением данных')
st.write('* реализовать streamlit-скрипт main.py, который возвращает случайные 10 позиций из csv-файла формате: автор - название книги')

st.write('-------------------------------------------------------------------------------------')
st.write('Релиз 2.0')
st.write('Срок: четверг, 17:00')
st.write('* сделать ipynb-файл с демонстрационным примером работы сервиса')

st.write('-------------------------------------------------------------------------------------')
st.write('Релиз 3.0')
st.write('Срок: пятница, 16:00')
st.write('* сделать main.py-файл, содержащий скрипт, реализующий streamlit-сервис')
st.write('* сделать README.MD, содержащий описание репозитория и способ запуска вашего сервиса')

st.write('-------------------------------------------------------------------------------------')
st.subheader('Рекомендации')
st.write('В качестве технологий стоит обратить внимание на:')
st.write('* библиотеку Sentence Transformers')
st.write('* языковые модели ruBERT (1,2)')
st.write('* поиск должен происходить максимально быстро, в этом может помочь faiss')
st.write('* рядом с каждым результатом выводите меру того, насколько он подходит под конкретный запрос')
st.write('* для улучшения качества поиска попробуйте отсечь слишком короткие аннотации')
st.write('* пробуйте использовать другие метрики близости – результат может отличаться в произвольную сторону')
st.write('* для уточнения поиска можно сделать дополнительное поле ввода (например, с автором)')
st.write('* в общем случае вы будете решать задачу симметричного семантического поиска: запрос должен быть подробным и по длине быть сопоставим с документами в хранилище. Это не всегда удобно: часто пользователю не хочется долго печатать, а значит его запрос будет короче описания объектов. Тогда можно рассмотреть модели для ассиметричного семантического поиска')
st.write('* Дополните сервис возможностью получать краткое содержание книги (Sber GigaChat, YandexGPT, парсинг с Википедии и тд).')
st.write('* Упакуйте свое приложение в docker-контейнер и разместите образ на docker hub. Чтобы контейнер весил не очень много, обратите внимание, что некоторые модели с hugging-face доступны по API (переходите в карточку модели, жмите кнопку Deploy и выбирайте Inference API (serverless): вам будет предоставлен код, по которому можно обратиться к модели).')
st.write('* и получить результат, за инференс будет отвечать сервис hf).')


































