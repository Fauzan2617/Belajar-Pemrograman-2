class Animal:
    def __init__(self,name,age,species) -> None:
        self.name = name
        self.age = age
        self.species = species
        
class Cat(Animal):
    
    @objectmethod
    def deskripsi (self):
        return f"{self.name} adalah kucing berjenis {self.species} yang sudah berumur {self.age} tahun"
    
    def suara (self):
        return "meow!"
    
myCat = Cat("Neko",3,"Persian")
