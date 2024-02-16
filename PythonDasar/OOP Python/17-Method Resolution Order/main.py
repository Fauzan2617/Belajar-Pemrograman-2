# Membahas misalkan nama method sama 

class A:
    def show(self):
        print("Ini adalah show A")

class B:
    def show (self):
        print("Ini adalah show B")

# Untuk eksekusi ketika ada dua def/method dengan nama yang sama maka
# Dia akan mengeksekusi berdasarkan urutan dari awal hingga akhir
# Contoh pada class c dibawah dia dari C untuk awal dan B untuk akhir
# Maka dia akan eksekusi dari C terlebih dahulu
class C(A,B):
    pass

objek = C()
objek.show()
help(objek)