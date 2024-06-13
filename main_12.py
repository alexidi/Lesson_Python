"""
Прочесть с помощью pandas файл
california_housing_test.csv, который находится в папке
sample_data
2. Посмотреть сколько в нем строк и столбцов
3. Определить какой тип данных имеют столбцы
"""

import pandas as pd

# data = pd.read_csv('california_housing_test.csv')
# mask = (data['population'] > 0) & (data['population'] < 500)
# new_data = data[mask]
# avg = new_data['median_house_value'].mean()
# print(avg)

"""Дан файл california_housing_train.csv.
Найти максимальное значение переменной "households" 
в зоне минимального значения переменной min_population 
и сохраните это значение в переменную max_households_in_min_population."""

data = pd.read_csv('california_housing_test.csv')
min_population = data['population'].min()
max_households_in_min_population = data[data['population'] == min_population]['households'].max()
print(max_households_in_min_population)
