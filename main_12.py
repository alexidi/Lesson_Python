import pandas as pd


data = pd.read_csv('california_housing_test.csv')
print(data.isnull().sum())
