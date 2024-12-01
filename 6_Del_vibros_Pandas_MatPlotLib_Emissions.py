# Выбросы и ошибочные данные - например человек с ростом 205 см при среднем 175см

import pandas as pd
import matplotlib.pyplot as plt
import tkinter

data = {'value': [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 55]} # создание списка
df = pd.DataFrame(data) # создание датафрейма

df.boxplot(column='value')# вывод графика на экран
plt.show() # вывод графика на экран

print(df.describe())

Q1 = df['value'].quantile(0.25) # вывод среднего
Q3 = df['value'].quantile(0.75) # вывод максимального
IQR = Q3 - Q1 # вывод IQR

downside = Q1 - 1.5 * IQR
upside = Q3 + 1.5 * IQR

df_new = df[(df['value'] >= downside) & (df['value'] <= upside)] # вывод выбросов

df_new.boxplot(column='value')


