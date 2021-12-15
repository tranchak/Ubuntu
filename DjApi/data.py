import pandas as pd
import numpy as np
import pycountry
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from yandex_translate import YandexTranslate # Используем класс YandexTranslate из модуля yandex_translate
from yandex_translate import YandexTranslateException # Используем класс YandexTranslateException из модуля yandex_translate

#вспомогательную функцию для генерации цветовой схемы. На входе
# функция принимает количество цветов, которое необходимо сгенерировать.
# Функция возвращает связный список с цветами.

# Размер надписей на графиках
PLOT_LABEL_FONT_SIZE = 14
# Генерация цветовой схемы
# Возвращает список цветов
def getColors(n):
    COLORS = []
    cm = plt.cm.get_cmap('hsv', n)
    for i in np.arange(n):
        COLORS.append(cm(i))
    return COLORS

def dict_sort(my_dict):
    keys = []
    values = []
    my_dict = sorted(my_dict.items(), key=lambda x:x[1], reverse=True)
    for k, v in my_dict:
        keys.append(k)
        values.append(v)
    return (keys,values)

df = pd.read_csv('results_CSV.csv', escapechar='`', low_memory=False)
df = df.replace({'shape':None}, 'unknown')

print(type(df))

import csv
with open('results_CSV.csv', encoding='utf-8') as r_file:
    # Создаем объект reader, указываем символ-разделитель ","
    file_reader = csv.reader(r_file, delimiter = ",")
    # Счетчик для подсчета количества строк и вывода заголовков столбцов
    count = 0
    # Считывание данных из CSV файла
    for row in file_reader:
        if count == 0:
            # Вывод строки, содержащей заголовки для столбцов
            print(f'Файл содержит столбцы: {", ".join(row)}')
        count += 1
    print(f'Всего в файле {count + 1} строк.')
    print(type(file_reader)) #класс csv.reader

    fieldnames = ['Number', 'Ball1', 'Ball2', 'Ball3', 'Ball4', 'Ball5', 'Ball6']
    file_reader = csv.DictReader(r_file, fieldnames=fieldnames)
    print(type(file_reader)) #преобразование в класс csv.DictReader
    for row in file_reader:
        if count == 0:
            # Вывод строки, содержащей заголовки для столбцов
            print(f'Файл содержит столбцы: {", ".join(row)}')
            print(f' {row["Number"]} - {row["Ball6"]}', end='')
        count += 1