class team:
    def set_tim(self,team):
        self.tim = team
        
    def showtim(self):
        print(self.tim)

class tipe_hero:
    def sethero(self,tipe):
        self.tipe = tipe
        
    def showtipe(self):
        print(self.tipe)

class hero(team,tipe_hero):
    def __init__(self,name,health) -> None:
        self.name = name
        self.health = health

siti = hero("Siti",100)
siti.set_tim("Kuning")
siti.sethero("Magic")

siti.showtim()
siti.showtipe()
