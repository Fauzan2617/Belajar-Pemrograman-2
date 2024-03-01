import numpy as np

a = np.array([1,2,3])
b = np.array([4,5,6])

# Stacking Array, Matrix menumpuk
c = np.hstack((a,b))
d = np.vstack((a,b))

print(c)
print(d)