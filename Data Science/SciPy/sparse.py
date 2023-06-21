from scipy import sparse
import numpy as np

# CSR-матрица
sample_csr = sparse.csr_matrix([[1, 2, 0], [0, 0, 3], [4, 0, 5]])
row = np.array([0, 2, 2, 0, 1, 2])
col = np.array([0, 0, 1, 2, 2, 2])
data = np.array([1, 2, 3, 4, 5, 6])

# CSС-матрица
sample_csc = sparse.csc_matrix((data, (row, col)), shape=(3, 3))

I = np.array([0,3,1,0])
J = np.array([0,3,1,2])
V = np.array([4,5,7,9])

# COO-матрица
sample_coo = sparse.coo_matrix((V,(I,J)),shape=(4,4))
# LIL матрица
sample_lil = sparse.lil_matrix((3, 3))

# DOK-матрица
sample_dok = sparse.dok_matrix((5, 5), dtype=np.float32)

from numpy.random import rand

sample_lil[0, :100] = np.ones(100)
sample_lil[1, 100:200] = sample_lil[0, :100]
sample_lil.setdiag(rand(1000))

for i in range(5):
    for j in range(5):
        sample_dok [i, j] = i + j

# Переведем в dense и исправим необходимые значения
tmp_filled = sample_csr.toarray()
tmp_filled[0, 0] = 10
sample_csr_new = sparse.csr_matrix(tmp_filled)

#Аналогично через сложение двух матриц
tmp_csr = sparse.csr_matrix([[5, 0, 0], [0, 0, 0], [0, 0, 0]])
sample_csr_new = sample_csr + tmp_csr

v = np.array([1, 0, -1])
	tmp_csr = sparse.csr_matrix([[5, 0, 0], [0, 0, 0], [0, 0, 0]])
sample_csr = sample_csr + tmp_csr
sample_csr = sample_csr.dot(v)
v = np.array([1, 0, -1])
	tmp_csc = sparse.csc_matrix([[5, 0, 0], [0, 0, 0], [0, 0, 0]])
sample_csc = sample_csc + tmp_cscsample_csc = sample_csc.dot(v)

sample_lil_tmp = sparse.lil_matrix((3, 3))sample_lil = sample_lil.dot(v) + sample_lil_tmp
