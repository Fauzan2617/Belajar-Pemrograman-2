# 1. Membuat kode dengan banyak statement 
# jangan dituliskan dalam satu baris

'''
DISARANKAN
'''
a = 10
b = 20
c = 30
print(a)
print(b)
'''
TIDAK DISARANKAN
'''
a,b,c = 10,20,30
print(a,b,c)

# 2. Notasi Fungsi
# Memberikan penjelasan yg lebih spesifik dibandingkan docstring pada Fungsi

yes:
    def luas_persegi(panjang:int = 10, lebar:int = none):
        hasil = panjang * lebar
        return hasil
    
no:
    def luas_persegi(panjang:int=10, lebar:int=none):
        hasil = panjang * lebar
        return hasil