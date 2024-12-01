# временные ряды

import pandas as pd
import numpy as np

dates = pd.date_range(start='2022-07-26', periods=10,freq='D') # дата c началом c периодом и днем

values = np.random.rand(10) # значени

df = pd.DataFrame({"Date": dates, "Value": values}) # создание датафрейма c значениями

df.set_index("Date", inplace=True) # установка индекса
print('______________________________')
print(df)
print('______________________________')

month = df.resample("ME").mean() # переход на период "Mесяц"
print(month)
print('______________________________')


