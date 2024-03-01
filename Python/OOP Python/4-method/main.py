class hero:
    jumlah_hero = 0
    
    def __init__(self,name,health) -> None:
        self.nama = name
        self.health = health
        
    def name(self):
        print("Namaku adalah : " + self.nama)
        
    def getup(self,up):
        self.health += up
        
    def gethealth(self):
        return self.health
    
bintang = hero("Bintang",120)

bintang.name()
bintang.getup(10)

print(bintang.gethealth())