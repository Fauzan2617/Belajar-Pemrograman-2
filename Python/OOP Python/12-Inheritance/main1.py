class hero():
    def __init__(self,nama):
        self.nama = nama
    
class magic(hero):
    pass

dwi = hero("fauzan")
putera = magic("putera")

print(dwi.nama)
print(putera.nama)