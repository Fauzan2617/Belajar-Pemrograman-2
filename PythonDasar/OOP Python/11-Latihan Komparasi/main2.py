class hero():
    def __init__(self,nama,health,atk,armor) -> None:
        self.__nama = nama
        self.__healthstandar = health
        self.__atkstandar = atk
        self.__armorstandar = armor
        self.__exp = 0
        self.__level = 1
    
        self.__healthmax = self.__healthstandar * self.__level
        self.__atkmax = self.__atkstandar * self.__level
        self.__armormax = self.__armorstandar * self.__level
        
        self.__healthstandar = self.__healthmax
        
        
    @property
    def info(self):
        print ("{} \n\t health = {}/{} \n\t atk = {} \n\t armor = {}".format(self.__nama,self.__healthstandar,self.__healthmax,self.__atkmax,self.__armormax))
    
    @property
    def gainexp(self):
        pass
    
    @gainexp.setter
    def gainexp(self,addexp):
        self.__exp += addexp
        if (self.__exp == 100):
            print(self.__nama + "Level UP")     
            self.__exp -= 100
            self.__level += 1
            
            self.__healthmax = self.__healthstandar * self.__level
            self.__atkmax = self.__atkstandar * self.__level
            self.__armormax = self.__armorstandar * self.__level
            siti.info

    @property
    def attack(self):
        pass
    
    @attack.setter
    def attack(self,musuh):
        print(self.__nama , "Menyerang", musuh)
        print(musuh , "Diserang", self.__nama)

        self.gainexp = 100
    

siti = hero("siti",100,10,20)
siti.attack = "dwi"