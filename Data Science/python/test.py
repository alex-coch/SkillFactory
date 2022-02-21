import pandas as pd

# users = pd.read_csv("users.csv", sep='\t', encoding='koi8-r')
# users.columns = ['user_id', 'email', 'geo']
# print(users)

# log = pd.read_csv('log.csv')
# log.columns = ['user_id', 'time', 'bet', 'win']
# new_log = log[~log.user_id.str.contains("error", na=False)]
# log2 = log.query('(bet < 2000) & (win > 0)')
# # log_win = log[log['win'] > 0]
# # win_count = len(log_win)
# print(new_log)

def profession_code(s):
    if s == 'Рабочий':
        o = 0
    elif s == 'Менеджер':
        o = 1
    else:
        o = 2
    return o

def age_category(age):
    if age < 23:
        o = 'молодой'
    elif 23 <= age < 35:
        o = 'средний'
    else:
        o = 'зрелый'
    return o


# sample = pd.read_csv('sample.csv')
# sample['Age_category'] = sample.Age.apply(lambda x: age_category(x))
# # # sample2 = sample
# # # sample4 = sample[~sample.City.str.contains("о", na=False)]
# # # # sample2 = sample[(sample['Age'] < 30) & (sample['Profession'] == 'Рабочий')]
# print(sample)

def userid(s):
    return s[-8:] if s.find('#error') == -1 else ''

log = pd.read_csv('log.csv', header=None)
log.columns = ['user_id','time','bet','win']
log.drop(log[log.user_id == '#error'].index, inplace=True)
log.user_id = log.user_id.apply(lambda x: x[-8:])
log.time = log.time.apply(lambda x: str(x)[1:] if str(x)[0] == '[' else x)
print(log)

t = log.time[0]
t = t[1:] if t[0] == '[' else t
print(t)
# import os
# files = os.listdir('data')
# print(files)

# for root, dirs, files in os.walk('data'):
#     print(root, dirs, files)
#
# files = ['setup.py', 'ratings.txt', 'stock_stats.txt', 'movies.txt', 'run.sh', 'game_of_thrones.mov']
# files = list(filter(lambda x: 'txt' in x, files))
# print(files)

# data = pd.DataFrame(columns = ['userId', 'movieId', 'rating', 'timestamp'])
# for filename in files:
#     temp = pd.read_csv( os.path.join('data', filename), names = ['userId', 'movieId', 'rating', 'timestamp'] )
#     data = pd.concat([data, temp])
# print(len(data))

# items_dict = {
#
#     'item_id': [417283, 849734, 132223, 573943, 19475, 3294095, 382043, 302948, 100132, 312394],
#
#     'vendor': ['Samsung', 'LG', 'Apple', 'Apple', 'LG', 'Apple', 'Samsung', 'Samsung', 'LG', 'ZTE'],
#
#     'stock_count': [54, 33, 122, 18, 102, 43, 77, 143, 60, 19]
#
# }
#
# purchase_log = {
#
#     'purchase_id': [101, 101, 101, 112, 121, 145, 145, 145, 145, 221],
#
#     'item_id': [417283, 849734, 132223, 573943, 19475, 3294095, 382043, 302948, 103845, 100132],
#
#     'price': [13900, 5330, 38200, 49990, 9890, 33000, 67500, 34500, 89900, 11400]
#
# }
#
# items_df = pd.DataFrame(items_dict)
# purchase_df = pd.DataFrame(purchase_log)
# df = items_df.merge(purchase_df, how='inner', on='item_id')
# df['col1'] = df['stock_count'] * df['price']
# print(df.col1.sum())

# data = pd.Series(list(range(10, 1001)))
# print(data.loc[10] + data.loc[23] - data.loc[245] + data.iloc[122])

# df = pd.read_csv('ratings.csv')
# # print(df.rating.value_counts())
# movies = pd.read_csv('movies.csv')
# df = df.merge(movies, on='movieId', how='outer')
# print(df[df['movieId'] == 3456])
# ratings = pd.read_csv('ratings_example.txt', sep = '\t')
# movies = pd.read_csv('movies_example.txt', sep = '\t')
# movies.drop_duplicates(subset = 'movieId', keep = 'first', inplace = True)

#print(df.iloc[0])
# print(ratings.merge(movies, how = 'left', on = 'movieId'))
#print(df.describe(include = ['object']))
# print(df.Value.min())

# df = df.pivot_table(values=['SprintSpeed'],
# index=['Club'],
# columns=['Position'],
# aggfunc='mean',
# margins=True,
# fill_value=0)

# val = df[df['Club'] == 'FC Barcelona'].groupby(['Nationality']).Balance.max()
# val = df.loc[df['Nationality'] == 'Dominican Republic'][['Name','Club','Wage','Age','ShotPower']]
# print(val)
# df = df.loc[df['Club'].isin(['FC Barcelona','Real Madrid','Juventus','Manchester United'])].pivot_table(values=['Name'],
# index=['Nationality'],
# columns=['Club'],
# aggfunc='count',
# fill_value=0)
# print(df[df['Club'] == 'Manchester City'])
# df = df.reindex(df['Position'].sort_values(by='ST', ascending=False).index)

# print(df.sort_values(by=[('SprintSpeed',  'ST')], ascending=False))
# .sort_values(by=[('SprintSpeed',  'CF')], ascending=False)