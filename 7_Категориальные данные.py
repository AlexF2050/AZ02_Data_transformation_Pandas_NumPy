# Категориальные данные — это данные, которые могут принимать одно из ограниченного набора значений.

import pandas as pd

data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'gender': ['female', 'male', 'male', 'male', 'female'],
    'department': ['HR', 'Engineering', 'Marketing', 'Engineering', 'HR']
}

df = pd.DataFrame(data)
print(df)
print('______________________________________')
# делаем категории

df['gender'] = df['gender'].astype('category')
df['department'] = df['department'].astype('category')

df['department'] = df['department'].cat.add_categories(['Finance'])
print(df['department'].cat.categories)
print('______________________________________')

df['department'] = df['department'].cat.remove_categories(['HR'])
print(df['department'].cat.categories)
print('______________________________________')
print(df)

# print(df['gender'].cat.categories)
# print('______________________________________')
# print(df['department'].cat.categories)
#
# print('______________________________________')
# print(df['department'].cat.codes)
#
# print('______________________________________')
#
