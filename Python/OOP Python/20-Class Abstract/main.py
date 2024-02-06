# Abstrack method memaksa si kelas pewaris untuk mengikuti  


# Membuat class abstrack
# Kita memanggil Abstract dengan import ABC
# abc =  Abstract base class
from abc import ABC,abstractmethod

# ABC dimasukan pada parameter class pertama/Super Class
class button(ABC):
    
# Lalu method click diberikan @abstractmethod agar dia menjadi fungsi abstract
# Maka untuk class yang mewarisi class super harus ada method yang sama dari class super (WAJIB) 
    @abstractmethod
    def click(self):
        pass

class clickbutton(button):

# Pada class kedua yang mewarisi class super dimana sudah menjadi class abstract
# Maka harus ada minimal satu def/method yang sama dari class super yang sudah diberi @abstractmethod
# Cukup satu aja, untuk method selanjutnya normal
    def click(self):
        print("Ini adalah clickbutton") 

    def click2(self):
        print("ini adalajh click button 2")

tombol1 = clickbutton()

tombol1.click()
tombol1.click2()