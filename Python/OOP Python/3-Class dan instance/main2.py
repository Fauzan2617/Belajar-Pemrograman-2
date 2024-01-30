class hero:
    def __init__(self,nama,health,armor) -> None:
        self.name = nama
        self.health = health
        self.armor = armor
        
    def show(self):
        print("{}\t {}Nama \t {}Armor".format(self.health,self.name,self.armor))
        

siti = hero("siti",100,50)
siti.show()