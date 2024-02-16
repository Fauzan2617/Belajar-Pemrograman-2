class hero:
    
    def __init__(self,name,health,armor) -> None:
        self.name = name
        self.__health = health
        self.__armor = armor
        # self.info = "name {} : \n\thealth {}".format(self.name,self.__health)
        
    @property
    def info(self):
            return "name {} : \n\thealth {}".format(self.name,self.__health)
        
        
    # FITUR GETTER, Hanya mengambil tapi tidak merubah
    @property
    def armor (self):
        pass
    
    @armor.getter
    def armor(self):
        return self.__armor
    
    @armor.setter
    def armor(self,input):
        self.__armor = input
        
    @armor.deleter
    def armor(self):
        print("Armor di Delete")
        self.__armor = None

print("\n MERUBAH INFO")
dwi = hero("Dwi",100,10) 
print(dwi.info)
dwi.name = "siti"
print(dwi.info)


print("\nFUNGSI GETTER DAN SETTER")
print(dwi.armor)
dwi.armor = 100
print(dwi.armor)

print("\n FUNGSI DELETE")
del dwi.armor
print(dwi.__dict__)