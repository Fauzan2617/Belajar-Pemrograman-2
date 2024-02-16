import numpy as np

a = np.array(([1,2,3],
              [4,5,6]
              ))


print('matrix a dengan ukuran :',a.shape ) # Fungsi shape untuk mengetahui ukuran si array
print(a)

# Transpose Matrix
# Transpose membuat yang baris menjadi kolom/Pembalikan
print("Transpose dari matrix A")
print(a.transpose())
print(np.transpose(a))
print(a.T)

# Flatten Array
# Membuat semua array menjadi baris ke kanan
print("Flatten matrix a")
print(a.ravel())
print(np.ravel(a))
print('matrix a dengan ukuran :',a.shape )

# Reshape Matrix
# Merubah ukuran namun tidak merubah ukuran default SHAPE
print("Reshape matrix a:")
print(a.reshape(3,2))
print('matrix a dengan ukuran :',a.shape )

# Resize Matrix
# Resize merubah ukuran default matrix ketika di SHAPE
print("Resize Matrix")
a.resize(3,2)
print(a)
print('matrix a dengan ukuran :',a.shape )
