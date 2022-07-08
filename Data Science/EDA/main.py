import numpy as np
from functools import reduce
import operator
import math

import pandas as pd
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()


vis_data = pd.read_csv("train.csv", encoding='ISO-8859-1', low_memory = False)
# print(vis_data.info())
res = scaler.fit_transform(np.array(vis_data.balance_due).reshape(-1, 1))
print(res.min())

exit(1)

df = pd.read_csv('data_flats.csv', sep=';')
df.dropna(inplace=True)
print(df.describe())
exit(1)

vis_data = pd.read_csv("train.csv", encoding='ISO-8859-1', low_memory = False)
result = vis_data.state.fillna(vis_data.state.mode())
exit(1)


data = pd.read_csv('data_flats.csv',sep=";")
print(data.head())
print(data.info())


array = np.array([i*i for i in range(100, 1000) if i % 2])
print(np.corrcoef(array[::2], array[1::2]))
exit(1)

my_array = np.array([[1,2,3,4,5],
                     [6,7,8,9,10],
                     [11,12,13,14,15],
                     [16,17,18,19,20],
                     [21,22,23,24,25]])
print(np.sum(np.array(list(map(math.sin, my_array.flatten()))).reshape(5, 5)[:, :4].reshape(10, 2)[:, 0]))
exit(1)

students = pd.read_csv('d:\\Book1.csv', sep=';')
# print(np.mean(df.mass) - np.median(df.mass))
# print(np.corrcoef(students['mass'], students['grade']))
# print(students['grade'])
print(pow(np.std(students['mass']), 2))
exit(1)