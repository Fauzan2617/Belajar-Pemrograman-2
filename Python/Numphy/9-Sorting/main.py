import numpy as np

a = np.floor(np.random.randn(1,6)*10)

print("nilai max dari a = ",a.max()) # Mencari nilai terbesar dari array
print("posisi max dari a = ", a.argmax()) # Mencari posisi index si nilai terbesar
print("Nilai min dari a = ", a.min()) # Mencari nilai terkecil dari array
print("Posisi min dari a = ", a.argmin()) # Mencari posisi dari si nilai terkecil

# Mensorting Array
print("Mengurutkan Array")
print(np.sort(a))
print(np.argsort(a))