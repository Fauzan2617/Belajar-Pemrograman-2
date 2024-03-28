class hero:
    def __init__(self,angka) -> None:
        self.__angka = angka
    
    def info_tambah(self):
        return self.__angka + self.__angka
    
    # Getter
    def get():
        return 
    
tambah = hero(150)
print(tambah.info_tambah())