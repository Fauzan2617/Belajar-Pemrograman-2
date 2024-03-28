from scipy import sparse
import numpy as np

a = np.eye(4)
print(a)

sparse_matrix = sparse.csr_matrix(a)
print(sparse_matrix)


