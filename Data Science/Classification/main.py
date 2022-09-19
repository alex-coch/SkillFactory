import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import log_loss

df = pd.read_csv('train_mobile.csv', sep=';')
# df.drop([0], axis=1, inplace=True)
df.reset_index(inplace=True)
df.dropna(how='all', inplace=True)
print(df.head(1))
# sns.heatmap(df)
# plt.show()

print(log_loss([0, 0, 1, 1], [0.2, 0.8, 1, 0.6], labels=None))