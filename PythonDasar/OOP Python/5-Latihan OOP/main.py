class hero:
    
    def __init__(self,name,health,atk) -> None:
        self.name = name
        self.health = health
        self.atk = atk
        
    def menyerang(self,lawan):
        print(self.name + "Menyerang" + lawan.name)
        lawan.diserang(self,self.atk)
        
    def diserang(self,lawan,atk_lawan):
        print(self.name + "diserang" + lawan.name)
        atk_diterima = self.health -+ atk_lawan
        print("attack diterima" + str(atk_diterima))
        print("Sisa darah " + str(atk_diterima))
        
        
        
diaz = hero("diaz",100,20)
novan = hero("novan",100,20)

diaz.menyerang(novan)
