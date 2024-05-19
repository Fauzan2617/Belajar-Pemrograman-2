'''
ATRIBUT CLASSS
'''

class mobil:
    warna = "merah"

mobil.warna = "hitam"
print(mobil.warna)

dwi = mobil()
print(dwi.warna)

arya = mobil()
print(arya.warna)

# -----------------------------------------------------------------------------------------------------------------------------------
'''
CLASS CONSTRUCTOR
'''
class mobil:
    def __init__(self,warna,kecepatan) -> None:
        self.warna = warna
        self.kecepatan = kecepatan

sedan = mobil("Merah",100)
print(sedan.kecepatan,sedan.warna)
# -----------------------------------------------------------------------------------------------------------------------------------
'''
CLASS DENGAN METHOD
'''
class mobil:
    def __init__(self,warna,kecepatan) -> None:
        self.warna = warna
        self.kecepatan = kecepatan
        
    def ubah_warna(self,ubah):
        self.warna = "hitam"
        return self.warna
        
sedan = mobil("hitam",100)
sedan.ubah_warna("Merah")
print(mobil.ubah_warna)