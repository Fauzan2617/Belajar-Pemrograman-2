# inheritance adalah pewarisan dari kelas 1 ke kelas 2 
# Kelas awal atau kelas 1 disebut kelas Super

class hero :
    
    def __init__(self,name,health) -> None:
        self.name = name
        self.health = health
        
class hero_streatgh(hero):
    pass

siti = hero("siti",100)
print(siti.name)

pajan = hero_streatgh("pajan", 100)
print(pajan.name)


print(help(pajan))