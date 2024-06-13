import random

import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
data.head()
print(data)

# Решение №1

data['tmp'] = 1
data.set_index([data.index, 'whoAmI'], inplace=True)
data = data.unstack(level=-1, fill_value=0).astype(int)
data.columns = data.columns.droplevel()
data.columns.name = None
print(data)

# Решение №2

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
new_data = pd.DataFrame()
new_data['robot'] = [1 if x == 'robot' else 0 for x in data['whoAmI']]
new_data['human'] = [1 if x == 'human' else 0 for x in data['whoAmI']]

print(new_data)
