class hero():
    def __init__(self,nama,health) -> None:
        self.__nama = nama
        self.__health = health
        
    
    def info(self):
        print("{},Health nya yaitu {}".format(self.__nama,self.__health))
        
    
class magic(hero):
    def __init__(self, nama, health) -> None:
        super().__init__(nama, health)
        super().info()
        
dwi = magic("dwi",100)