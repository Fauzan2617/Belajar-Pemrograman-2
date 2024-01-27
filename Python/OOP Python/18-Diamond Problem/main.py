# Diamond Problem

class A :
    def show(self):
        print("Ini ada shofinfo class A")

class B(A):
    def show(self):
        print("Ini ada shofinfo class B")

class C(A):
    def show(self):
        print("Ini ada shofinfo class B")

class D(B,C):
    pass

objek = C()
objek.show()