import numpy as np

# Perkalian Biasa
matriks1 = np.array ([[1,2,3,4,5],
            [6,7,8,9,10],
            [11,12,13,14,15]])

matriks2 = [[0 for i in range (5)] for j in range (3)]

for i in range(len(matriks1)):
    for j in range(len(matriks1[0])):
        matriks2[i][j] = matriks1[i][j] * 2
        
print(matriks2)

# Kali dengan menggunakan fitur array
result = matriks1 * 2
print(result)