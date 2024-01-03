class hero:
    __jumlah = 0
    
    def __init__(self,nama,health,attack,armor) -> None:
        self.__nama = nama
        self.__healthstandar = health
        self.__attackstandar = attack
        self.__armorstandar = armor
        self.__exp = 0
        self.__level = 1
        
        self.__healthmax = self.__healthstandar * self.__level
        self.__attackmax = self.__attackstandar * self.__level
        self.__armormax = self.__armorstandar * self.__level
        
        self.__health = self.__healthmax
        self.__jumlah += 1
        
    @property
    def info(self):
        return "{} \n\tHealth = {}/{} \n\tattack = {} \n\tarmor = {}".format(self.__nama,self.__health,self.__healthmax,self.__attackmax,self.__armormax)
    
    @property
    def gainexp(self):
        pass
    
    @gainexp.setter
    def gainexp(self,addexp):
        self.__exp += addexp
        if(self.__exp == 100):
            print(self.__nama, "Level UP ")
            self.__level += 1
            self.__exp -= 100
            
            self.__healthmax = self.__healthstandar * self.__level
            self.__attackmax = self.__attackstandar * self.__level
            self.__armormax = self.__armorstandar * self.__level
    
    @property
    def attack(self):
        pass
    
    @attack.setter
    def attack(self,musuh):
        print(self.__nama , "Menyerang", musuh)
        print(musuh , "Diserang", self.__nama)

        self.gainexp = 100
    
dwi = hero("fauzan",100,10,20)
siti = hero("uji",100,10,20)
print(dwi.info)

dwi.attack = "siti"
print(dwi.info)
    
    
    