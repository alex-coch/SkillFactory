import numpy as np

a = np.matrix([[1, 2], [-3, 1], [1, 2], [1, -1]])
b = np.matrix([1, 4, 5, 0]).reshape(4,1)
w = np.linalg.inv(a.T.dot(a)).dot(a.T).dot(b)
# e = b - a.dot(w)
print(w)