class hero:
    def __init__(self,name,health,atk) -> None:
        self.nama = name
        self.health = health
        self.atk = atk
        
    def menyerang(self,lawan):
        print(self.nama, "Menyerang", lawan)
        lawan.diserang(self,self.atk)
        
    def diserang(self,lawan,atk):
        print(self.nama, "Diserang", lawan)
        health = self.health - atk
        print("Atk yang diterima" + str(atk))
        print("Sisa darah yaitu ", str(health))


pram = hero("Pram",100,20)
dan = hero("dan",100,20)

pram.menyerang(dan)