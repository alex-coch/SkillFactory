import pandas as pd


# data = pd.Series(list(range(10, 1001)))
# print(data.loc[10] + data.loc[23] - data.loc[245] + data.iloc[122])

df = pd.read_csv('data_sf.csv')
#print(df.iloc[0])
# print(df.info())
#print(df.describe(include = ['object']))
# print(df.Value.min())

df = df.pivot_table(values=['SprintSpeed'],
index=['Club'],
columns=['Position'],
aggfunc='mean',
margins=True,
fill_value=0)

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

print(df.sort_values(by=[('SprintSpeed',  'ST')], ascending=False))
# .sort_values(by=[('SprintSpeed',  'CF')], ascending=False)