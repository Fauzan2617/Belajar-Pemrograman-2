import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10,10,100)
y = np.sin(x)

# Inisialisasi/Pembuatan plot objek
plt.plot(x,y)

# Memunculkan 
plt.show()