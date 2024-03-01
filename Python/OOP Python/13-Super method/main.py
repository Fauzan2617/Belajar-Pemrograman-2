class hero:
    def __init__(self,name,health) -> None:
        self.nama = name
        self.health = health
        
    def info(self):
        print("{} Health nya adalah = {}".format(self.nama,self.health))
        
class herostreaght(hero):
    def __init__(self, name, health) -> None:
        # super dibawah, mengambil dari class super (hero) diatas
        # Pada super() dibawah ketika memanggil dan memasukkan data, data akan masuk ke class SUPER (class hero)
        super().__init__(name, health)
        super().info()
        
class heromage(hero):
    def __init__(self, name, health) -> None:
        super().__init__(name, health)
        super().info()

dwi = herostreaght('dwi',100)
siti = heromage('siti',100)