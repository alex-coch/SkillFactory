import numpy as np
from functools import reduce
import operator
import math

import pandas as pd


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