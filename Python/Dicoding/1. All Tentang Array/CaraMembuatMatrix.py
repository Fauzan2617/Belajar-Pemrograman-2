import numpy as np

# Membuat Matriks dengan deklarasi + nilai
matriks1 =  [[1,2,3,4,5],
            [6,7,8,9,10],
            [11,12,13,14,15]]

# Mengambil data dalam python pakai indexing
data_array = matriks1[1][2]
print(data_array)

# Membuat Array dengan deklarasi nilai default 0
matriks = [[0 for j in range(4)]for i in range(3)]
print(matriks)

