# ONE LIER
# Sebuah pemrograman dengan hanya satu baris
a = 10
b = 20
print (a,b)
a,b = b,a # <-- Pertukaran Data di Python
print (a,b)

print("="*80)

#--------------------------------------------------------------
#PENGULANGAN
# Variable kosong dianggap FALSE
# Variable isi dianggap TRUE
a = ""
if a:
    print("True")
else :
    print("False")
# One Liner dalam pengulangan
Score = 100
if Score == 100 : print("Halooo")
# One liner ketika if,elif,dan else
lulus = True
kelulusan = ("Perbaiki, Anda belum lulus.","Selamat, Anda lulus!")[lulus]
print(kelulusan)
# For untuk pengulangan
# RANGE
for i in range(1,10):
    print(i)
# Range (Start,Stop,Lompatan)
print("="*80)
# For untuk membuat mengisi variable baru
angka = [1,2,3,4,5]
var_new = [n**2 for n in angka]
print(var_new)
for i in range(1, 3):    
    for j in range(1, 3):    
        print(i,j) 