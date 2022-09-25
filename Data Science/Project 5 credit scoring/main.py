import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.feature_selection import f_classif, mutual_info_classif
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

data = pd.read_csv('train.csv')
data.education.fillna('SCH', inplace=True)
# print(data.iloc[0])
train, validation = train_test_split(data, test_size=0.33, random_state=42)

#бинарные переменные
bin_cols = ['sex', 'car', 'car_type', 'good_work', 'foreign_passport']

#категориальные переменные
cat_cols = ['education', 'work_address', 'home_address']

#числовые переменные
num_cols = ['age', 'decline_app_cnt', 'bki_request_cnt', 'income']
# num_cols = ['income']

for i in num_cols:
    plt.figure()
    # train[i] = np.log(train[i])
    sns.histplot(train[i][train[i] > 0].dropna(), kde = False)
    plt.title(i)
#     plt.show()

df = train[train.default ==0]
for i in num_cols:
    plt.figure()
    # df[i] = np.log(df[i])
    sns.boxplot(df[i])
    plt.title(i)
#     plt.show()

sns.heatmap(train[num_cols].corr().abs(), vmin=0, vmax=1)
# plt.show()

imp_num = pd.Series(f_classif(train[num_cols], train['default'])[0], index = num_cols)
imp_num.sort_values(inplace = True)
imp_num.plot(kind = 'barh')
# plt.show()

label_encoder = LabelEncoder()
mapped_education = pd.Series(label_encoder.fit_transform(train['sex']))
# print(dict(enumerate(label_encoder.classes_)))

# Для бинарных признаков мы будем использовать LabelEncoder
label_encoder = LabelEncoder()
# print(train[bin_cols].head())
for column in bin_cols:
    train[column] = label_encoder.fit_transform(train[column])
# убедимся в преобразовании
# print(train[bin_cols].head())

X_cat = OneHotEncoder(sparse = False).fit_transform(train[cat_cols].values)
print(X_cat.shape)