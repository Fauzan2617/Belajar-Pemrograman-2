import numpy as np

dtipe = [("Nama","S255"),("Tinggi",int)]
data = [
    ("Dwi",150),
    ("Fauzan",120),
    ("Putera",100)
        
        ]
a = np.array(data , dtype=dtipe)

'''
a = np.sort(a,order="Tinggi")
print(a)
'''