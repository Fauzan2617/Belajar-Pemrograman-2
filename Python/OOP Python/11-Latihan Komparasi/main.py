class hero :
    
    # Private Class VARIABLE
    __jumlah = 0
    
    def __init__(self,name,health,attpower,armor) -> None:
        self.__name = name
        self.__healthstandar = health
        self.__attpowerstandar = attpower
        self.__armorStandar = armor
        self.__level = 1
        self.__exp = 0
        
        self.__healthMax = self.__healthstandar * self.__level
        self.__attpower = self.__attpowerstandar * self.__level
        self.__armor = self.__attpowerstandar * self.__level
        
        self.__health = self.__healthMax
        
        hero.__jumlah += 1
        
    @property
    def info (self):
        return "{}: level = {} \n\thealth = {}/{} \n\tattack = {} \n\tarmor = {}".format(self.__name,self.__level,self.__health,self.__healthMax,self.__attpower,self.__armor)
    
    @property
    def gainEXP(self):
        pass
    
    @gainEXP.setter
    def gainEXP(self,addexp):
        self.__exp += addexp
        if (self.__exp >= 100):
            print(self.__name, "Level Up")
            self.__level += 1
            self.__exp -= 100
            
            self.__healthMax = self.__healthstandar * self.__level
            self.__attpower = self.__attpowerstandar * self.__level
            self.__armor = self.__attpowerstandar * self.__level
    
    @property
    def attack(self):
        pass
    
    @attack.setter
    def attack(self,musuh):
        print(self.__name , "Menyerang", musuh)
        print(musuh , "Diserang" , self.__name)
        
        self.gainEXP = 100
        
        
siti = hero("siti",100,50,20)
pajan = hero("pajan",100,50,20)
print(siti.info)

siti.attack = "pajan"
print(siti.info)