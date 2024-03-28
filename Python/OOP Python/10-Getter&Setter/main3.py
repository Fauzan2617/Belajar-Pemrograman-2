class hero():
    def __init__(self,nama,health) -> None:
        self.__health = health
        self.__nama = nama
        
    @property
    def infohero(self):
        print("Nama Hero {}, Jumlah Health {}".format(self.__nama,self.__health))
        
    @property
    def gethealt():
        pass
    
    @gethealt.getter
    def gethealt(self):
        return self.__health
    
    @property
    def getname(self):
        pass
    
    @property
    def rubahhealth(self):
        pass
    
    @rubahhealth.setter
    def rubahhealth(self,uphealth):
        self.__health += uphealth
    
    @getname.getter
    def getname(self):
        return self.__nama
    

ahmad = hero("Ahmad",100)
ahmad.rubahhealth = 200
print(ahmad.infohero)
