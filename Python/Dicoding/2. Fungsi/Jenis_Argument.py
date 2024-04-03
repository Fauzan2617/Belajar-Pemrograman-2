# Argument dalam Python
'''
1. Keyword Argument 
Jenis Argument yang ketika fungsi dipanggil dan memasukkan data, nama parameter nya diikutkan
'''
def hitung_luas_persegi(panjang,lebar):
    result = panjang * lebar
    return result

hasil = hitung_luas_persegi(panjang= 10,lebar= 20) # Contoh
print(hasil)

'''
2. Positional Argument
Jenis Argument yang tidak menyebutkan parameter namun perlu mengikuti urutan parameter
'''
def hitung_luas_persegi(panjang,lebar):
    result = panjang * lebar
    return result

hasil = hitung_luas_persegi(10,20) # Contoh
print(hasil)
