import pandas as pd


# data = pd.Series(list(range(10, 1001)))
# print(data.loc[10] + data.loc[23] - data.loc[245] + data.iloc[122])

df = pd.read_csv('data_sf.csv')
#print(df.iloc[0])
#print(df.info())
#print(df.describe(include = ['object']))
# print(df.Value.min())

val = df[df.Aggression == df.Aggression.max()].ShotPower.mean() / df[df.Aggression == df.Aggression.min()].ShotPower.mean()

print(val)
