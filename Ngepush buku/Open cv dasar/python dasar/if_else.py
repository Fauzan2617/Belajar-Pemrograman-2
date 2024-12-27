#1 
# bilangan = int(input("Masukkan bilangan bulat: "))
# type_bilangan = "genap" if bilangan % 2 == 0 else "ganjil"
# print(f"Bilangan {bilangan} adalah bilangan {type_bilangan}")


#2 if else bertingkat
# bilangan_input = input("masukkan angka :")
# bilangan = int(bilangan_input)
# if  bilangan % 2 == 0:
#     print ("ini genap")
# elif bilangan % 2 == 1:
#     print ("ini ganjil")
# elif bilangan == int:
#     print ("ini bukan int")
# else:
#     print("anda salah memasukkan angka")
    
    
#3 if else bersarang (dalam menentukan segitiga siku siku)
# print ("menghitung segitiga siku siku ")
# sisia = float(input("masukkan sisi 1 :"))
# sisib = float(input("masukkan sisi 2 : "))
# sisic =  float (input("masukkan sisi 3 : "))

# segitigasikusiku = False
# toleransi = 0.00001
# jumlahkuadrat = sisia * sisia + sisib * sisib
# ckuadrat = sisic * sisic

# if (jumlahkuadrat >= ckuadrat - toleransi) and (jumlahkuadrat <= ckuadrat + toleransi) :
#     segitigasikusiku = True
# else:
#     jumlahkuadrat = sisia * sisia + sisic * sisic
#     ckuadrat = sisib * sisib
#     if (jumlahkuadrat >= ckuadrat - toleransi) and (jumlahkuadrat <= ckuadrat + toleransi) :
#         segitigasikusiku = True
#     else:
#         jumlahkuadrat = sisib * sisib + sisic * sisic
#         ckuadrat = sisia * sisia
#         if (jumlahkuadrat >= ckuadrat - toleransi) and (jumlahkuadrat <= ckuadrat + toleransi) :
#             segitigasikusiku = True
            
# print ("hasil dari segitiga")
# if segitigasikusiku:
    
#     print (f"segitiga nya true ")
# else :
#     print ("bukan segitiga siku siku")
    
    
#3 perulangan while
# angka = 1
# while angka <= 10:
#     print (angka)
#     angka = angka + 1
    
#4 while untuk segitiga siku siku
# baris = 1
# tinggi = int(input("tinggi segitiga :"))
# while baris <= tinggi:
#     kolom = 1
#     while kolom <= baris:
#         print ("*" + ' ')
#         kolom = kolom + 1

#     print ()

#     baris = baris + 1
        
#5 fungsi dengan return
# def ganjil_true (bilangan):
#     hasil = bilangan % 2
#     return (hasil == 1 , "/t" , "INI ADALAH GANJIL")

# print ("angka 7" , ganjil_true(7))



#6 variabel global

# variable global biasanya tidak disarankan
def mobil():
    global merk 
    merk = "[pajero sport]"
    print ("mobil : ", merk)


merk = "fortuner"
print ("mobil semula :", merk)

mobil()
print ("mobil sekrang yaitu :", merk)    


#7 