from sklearn import metrics
import numpy as np

x = np.array([1.23, 2.35, 2.75])
y = np.array([1.01, 12.3, 2.74])
print(metrics.mean_squared_error(y, x))

# rss = np.sum((y - x) ** 2)
# tss = np.sum((y - y.mean()) ** 2)
# print(1 - rss / tss)