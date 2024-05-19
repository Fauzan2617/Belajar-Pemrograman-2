from abc import ABC,abstractmethod

class hero(ABC):
    
    @abstractmethod
    def click(self):
        pass
    
class anak(hero):
    def click(self):
        print("Ini adalah click 1")
    
    def click2(self):
        print("Ini adalah click button 2")

button = anak()
button.click()
button.click2()
