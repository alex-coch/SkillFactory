import numpy as np
from functools import reduce
import operator
import math

import pandas as pd
from sklearn.preprocessing import StandardScaler

# %matplotlib inline

vis_data = pd.read_csv("train.csv",
                       encoding = 'ISO-8859-1',
                       low_memory = False)
vis_data.balance_due.dropna(inplace=True)
def outliers_iqr(ys):
    quartile_1, quartile_3 = np.percentile(ys, [25, 75])
    iqr = quartile_3 - quartile_1
    lower_bound = quartile_1 - (iqr * 1.5)
    upper_bound = quartile_3 + (iqr * 1.5)
    return np.where((ys <= upper_bound) | (ys >= lower_bound))[0]

vis_data[outliers_iqr(vis_data.balance_due)].dropna(inplace=True)
res = vis_data.balance_due
print(res.max() - res.min())
exit(1)

vis_data = vis_data.drop(['violation_zip_code', 'clean_up_cost'], axis=1)
latlons = pd.read_csv("latlons.csv")
vis_data = pd.concat([vis_data, latlons], axis=1)
print(vis_data.info())
exit(1)

from sklearn.preprocessing import PolynomialFeatures

pf = PolynomialFeatures(2)
poly_features = pf.fit_transform(vis_data[['balance_due', 'payment_amount']])
print(poly_features)
print(poly_features.shape)

print(pd.get_dummies(vis_data.state).shape)

datetime_vals = pd.to_datetime(vis_data.payment_date.dropna())
print(datetime_vals.head())


exit(1)


df = pd.read_csv("train.csv", encoding='ISO-8859-1', low_memory=False)
df = df[df.balance_due > 0]
balance_due = pow(df.balance_due, 0.5)
print(balance_due.median() - balance_due.mean())
exit(1)


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