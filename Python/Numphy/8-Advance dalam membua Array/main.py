import numpy as np

# Membuat Array dengan tipe data tertentu, menggunakan DTYPE
a = np.array(([1,2,3],[4,5,6]), dtype= float)

# Membuat Array dengan fuction

def kuadrat(baris,kolom):
    return kolom**2

b = np.fromfunction(kuadrat,(1,10),dtype=int)
print(b)

# Membuat array dengan iterable
iterable = (x*2 for x in range(5))

c = np.fromiter(iterable,dtype=int)

# Multitype Array
dtipe = [("nama","S255"),("Tinggi",int)]

data = [
    ("Fauzan",150),
    ("Arya",120),
    ("Diaz",150)
]

d = np.array(data, dtype= dtipe)

print(d)