import numpy as np

# List biasa Python
a = [1,2,3,4,5]
b = [6,7,8,9,10]

# Elemen Array
anp = np.array([1,2,3,4,5])
bnp = np.array([6,7,8,9,10])

# ELEMENWISE (Dimana akan dijumlahkan per komponennya jika memakai arraay dari Numphy)
# Penjumlahan
hasil_Penjumlahan = anp+bnp
print(hasil_Penjumlahan)

# Pengurangan
hasil_pengurangan = anp-bnp
print(hasil_pengurangan)

# Perkalian
hasil_perkalian = anp*bnp
print(hasil_perkalian)

# Pembagian
hasil_pembagian = anp*bnp
print(hasil_pembagian)

# Kuadrat
hasil_kuadrat = anp**2
print(hasil_kuadrat)

# Multidimensi
c = np.array(([1,2,3],[4,5,6]))
d = np.array(([7,8,9],[-1,-2,-3]))
hasil = c+d 
hasil = c*d
print(hasil)


