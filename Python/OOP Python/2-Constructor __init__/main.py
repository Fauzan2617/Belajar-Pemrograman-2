class hero:
    
    def __init__(self,health,atk) -> None:
        self.health = health
        self.atk = atk
        


hikmal = hero(100,100)

print(hikmal.__dict__)
print(hikmal.health)