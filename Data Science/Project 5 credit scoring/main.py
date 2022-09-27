import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.feature_selection import f_classif, mutual_info_classif
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, roc_auc_score, roc_curve, auc, classification_report
from sklearn.model_selection import GridSearchCV

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

X_num = StandardScaler().fit_transform(train[num_cols].values)
X_train = np.hstack([X_num, train[bin_cols].values, X_cat])
y_train = train['default'].values

# validation
for column in bin_cols:
    validation[column] = label_encoder.fit_transform(validation[column])
X_cat = OneHotEncoder(sparse = False).fit_transform(validation[cat_cols].values)
X_num = StandardScaler().fit_transform(validation[num_cols].values)
X_validation = np.hstack([X_num, validation[bin_cols].values, X_cat])
y_true = validation['default'].values
validation.drop(['default'], axis=1, inplace=True)
# print(y_true)

model = LogisticRegression(random_state=0).fit(X_train, y_train)
y_pred = model.predict(X_validation) # _proba
# print(y_pred)

print(confusion_matrix(y_true, y_pred))

# roc_auc = roc_auc_score(y_true, y_pred)
# fpr, tpr, threshold = roc_curve(y_true, y_pred)

# plt.figure()
# plt.plot([0, 1], label='Baseline', linestyle='--')
# plt.plot(fpr, tpr, label = 'Regression')
# plt.title('Logistic Regression ROC AUC = %0.3f' % roc_auc)
# plt.ylabel('True Positive Rate')
# plt.xlabel('False Positive Rate')
# plt.legend(loc = 'lower right')


probs = model.predict_proba(X_validation)
preds = probs[:,1]
fpr, tpr, threshold = roc_curve(y_true, preds)
roc_auc = auc(fpr, tpr)

# method I: plt
plt.title('Receiver Operating Characteristic')
plt.plot(fpr, tpr, 'b', label = 'AUC = %0.2f' % roc_auc)
plt.legend(loc = 'lower right')
plt.plot([0, 1], [0, 1],'r--')
plt.xlim([0, 1])
plt.ylim([0, 1])
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
# plt.show()

print(classification_report(y_true, y_pred))

model = LogisticRegression()

iter_ = 50
epsilon_stop = 1e-3

param_grid = [
    {'penalty': ['l1'],
     'solver': ['liblinear', 'lbfgs'],
     'class_weight':['none', 'balanced'],
     'multi_class': ['auto','ovr'],
     'max_iter':[iter_],
     'tol':[epsilon_stop]},
    {'penalty': ['l2'],
     'solver': ['newton-cg', 'lbfgs', 'liblinear', 'sag', 'saga'],
     'class_weight':['none', 'balanced'],
     'multi_class': ['auto','ovr'],
     'max_iter':[iter_],
     'tol':[epsilon_stop]},
    {'penalty': ['none'],
     'solver': ['newton-cg', 'lbfgs', 'sag', 'saga'],
     'class_weight':['none', 'balanced'],
     'multi_class': ['auto','ovr'],
     'max_iter':[iter_],
     'tol':[epsilon_stop]},
]

## model ваша модель логистической регрессии
gridsearch = GridSearchCV(model, param_grid, scoring='f1', n_jobs=-1, cv=5)
gridsearch.fit(X_train, y_train)
model = gridsearch.best_estimator_

##печатаем параметры
best_parameters = model.get_params()
for param_name in sorted(best_parameters.keys()):
        print('\t%s: %r' % (param_name, best_parameters[param_name]))

y_pred = model.predict(X_validation) # _proba
# print(y_pred)
print(confusion_matrix(y_true, y_pred))