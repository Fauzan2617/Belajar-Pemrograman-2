from abc import ABC,abstractmethod

class A(ABC):
    def __init__(self,self_link) -> None :
        self.link = self_link
        
    @abstractmethod
    def click (self):
        pass
    
    @property
    @abstractmethod
    def link (self):
        pass
    
class b(A):
    def click(self):
        print("Silahkan ke : {}".format(self.link))
    
    @A.link.setter
    def link (self,input):
        self.__link = input
        
    @link.getter
    def link (self):
        return self.__link
    
object = b("www.fauzan.com")
object.click()