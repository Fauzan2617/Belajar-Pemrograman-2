# Multiple Ihretence :
# Dimana suatu class bisa mendapatkan warisan dari kelas Super lebih dari 1

class A:
    def method_A(self):
        print("Ini adalah method A")
class B:
    def method_B(self):
        print("Ini adalah method B")

# Dibawah ini dia adalah multiple Ihretence
# Menerima dari class A dan B
class sesuatu(A,B):
    pass

objek = sesuatu()
objek.method_A()
objek.method_B()