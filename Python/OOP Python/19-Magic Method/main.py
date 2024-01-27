class mangga:
    # Magic Method
    def __init__(self,nama,jumlah) -> None:
        self.__nama = nama
        self.__jumlah = jumlah
    
    # Method Dibawah dapat mengambil isi dari dari tiap self
    # Self private atau self umum
    # Method repr biasanya untuk debugging dan STR untuk program sudah berjalan
    def __repr__(self) -> str:
        return "Mangga: {} dengan jumlah: {}".format(self.__nama,self.__jumlah)
    
    def __str__(self) -> str:
        return "Mangga: {} dengan jumlah: {}".format(self.__nama,self.__jumlah)
# =========================================================================================================================

    # method add bisa menjumlahkan,mengurangi,perkalian dan pembagian
    # Intinya di berguna untuk aritmatika
    def __add__(self,objek):
        return self.__jumlah + objek.__jumlah


belanja1 = mangga("Ambon",100)
belanja2 = mangga("Arumanis",50)
print(belanja1)
print(belanja1 + belanja2)