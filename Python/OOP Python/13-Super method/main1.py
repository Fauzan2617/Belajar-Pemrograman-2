class hero():
    def __init__(self,nama,health) -> None:
        self.name = nama
        self.health = health
    
    def info(self):
        print("{} \n\t health = {} \n\t".format(self.name,self.health))
        
class magic(hero):
    def __init__(self, nama, health) -> None:
        super().__init__(nama,health)
        super().info()

siti = magic("siti",100)