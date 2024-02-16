import numpy as np

# Membuat vector
a = np.array([1,2,3,4,5])
b = np.array([1.5,2.5,5,6,7])

# Membuat vector dengan range
c = np.arange(1,10,2)

# Membuat linspace
d =  np.linspace(1,10,4)

# array multimendisi/matrix
e = np.array ([(1,2,3),(4,5,6)])
print(e)

# Matrix dengan nilai nol
f = np.zeros(5)

# Matrix dengan nilai 1
g = np.ones(1)

# Matrix identitas
h1 = np.eye(5)
h2 = np.identity(10)

print(h1)

