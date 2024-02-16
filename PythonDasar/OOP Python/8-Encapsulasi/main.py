class hero:
    
    def __init__(self,name,heatlh,atk) -> None:
        self.__name = name
        self.__health = heatlh
        self.__atk = atk
    
    # GETTER UNTUK MENDAPATKAN NILAI PADA VARIABLE PRIVATE
    # SETTER UNTUK MERUBAH NILAI PADA VARIABLE PRIVATE TANPA MERUBAH DATA ASLINYA
    # Getter:
    def gethealth(self):
        return self.__health
    
    def getname(self):
        return self.__name
    
    # Setter
    def menyerang(self,atk):
        self.__health -= atk
        
    
iqi = hero("iqi",100,20)

print(iqi.getname())
print(iqi.gethealth())
iqi.menyerang(10)
print(iqi.gethealth())