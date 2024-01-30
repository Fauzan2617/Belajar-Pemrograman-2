class hero:
    def __init__(self,name,health) -> None:
        self.__name = name
        self.__health = health
        
    def name(self):
        return self.__name
    
    def health(self):
        return self.__health
    
    
dwi = hero("hero",100)
print(dwi.health())
print(dwi.name())