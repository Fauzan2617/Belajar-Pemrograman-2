# Diamond Problem
class A:
    pass

class B(A):
    def show (self):
        print("Ini Adalah B")
    
class C(B,A):
    pass
    # def show (self):
    #     print("Ini adalah C")
    
object = C()
object.show()
