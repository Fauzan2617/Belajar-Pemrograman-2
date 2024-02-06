import numpy as np

a = np.arange(10)**2
# Mengambil Nilai
print("Elemen ke 1 dari adalah",a[1])
print("Elemen ke 2 dari a adalah",a[3])

# Slicing
print("elemen dari 1-6 adalah",a[0:5]) #[Start,End] 5 itu bukan akhir tapi batas sebelum indeks ke 5
print("Elemen dari 4 hingga akhir",a[4:])
print("Elemen dari awal sampe 5",a[:6])

# Iterasi
for i in a:
    print("i ke",i)






