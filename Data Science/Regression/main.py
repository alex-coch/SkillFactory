from sklearn import metrics
import numpy as np

x = np.array([1, 3, 2, 5])
y = np.array([2, 3, -1, 4])
print(metrics.r2_score(y, x))

rss = np.sum((y - x) ** 2)
tss = np.sum((y - y.mean()) ** 2)
print(1 - rss / tss)