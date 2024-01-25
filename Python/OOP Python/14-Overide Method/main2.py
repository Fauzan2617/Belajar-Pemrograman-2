class hero:
    def __init__(self,name,health):
        self.name = name
        self.health = health
    
    def showinfo(self):
        print("Show Info di kelas super")
        print("{} Nama Hero\t {} Health Hero".format(self.name,self.health))
        
class magic(hero):
    def __init__(self, name, health):
        super().__init__(name, health)
    
    def showinfo(self):
        print("Shof info di class magic")
        print("{} Nama Hero\t {} Health Hero".format(self.name,self.health))



Siti = magic("siti",100)
Siti.showinfo()