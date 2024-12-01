# Выбросы и ошибочные данные - например человек с ростом 205 см при среднем 175см

import pandas as pd
import matplotlib.pyplot as plt

data = {'value': [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 55]} # создание списка
df = pd.DataFrame(data) # создание датафрейма

df['value'].hist()
plt.show() # вывод графика на экран


