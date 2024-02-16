#index,Slicing,Iterasi
import numpy as np

a = np.arange(10)**3

# Mengambil Array berdasarkan Index
print("Array ke 4 adalah",a[4])
print("Array ke 8 adalah",a[8])

# Mengambil Array berdasarkan Slicing
print("Array dari 1 hingga akhir adalah", a[1:]) 
print("Array dari awal hingga 7 adalah", a[:7])
print("Array dari 2 ke 5", a[2:5])

# Mengambil Array dengan iterasi
for i in a:
    print(i)