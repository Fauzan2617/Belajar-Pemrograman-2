# Manipulasi Array dengan Transpose,Flatten,Resize,dan Reshape
import numpy as np

a = np.array(([1,2,3,
            4,5,6],
            [7,8,9,
            10,11,12]))

print("Panjang dari Array a adalah", np.shape(a))


# Transpose Array
print("Transpose Array/Pembalikan")
print(np.transpose(a))
print(a.transpose())
print(a.T)

# Flatten
print("Flatt kepada Array")
print(np.ravel(a))
print(a.ravel())

# Reshape
print("Reshape kepada Array")
print(a.reshape(6,2))

# Resize
print("Resize kepada Array")
a.resize(6,2)
print(a)