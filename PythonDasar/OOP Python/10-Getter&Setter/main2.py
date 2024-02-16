class hero:
    def __init__(self,name,health) -> None:
        self.__nama = name
        self.__heatlh = health
        
        
    @property
    def showinfo(self):
        return "{}nama \t {}heatlh".format(self.__nama,self.__heatlh)
    
    @property
    def getname(self):
        pass
    
    @getname.getter
    def getname(self):
        return self.__nama
    
    @property
    def gethealth(self):
        pass
    
    @gethealth.setter
    def gethealth(self,uphealth):
        self.__heatlh += uphealth
        
print("MERUBAH INFO")
bintang = hero("bintang",100)
bintang.gethealth = 100
print(bintang.showinfo)

