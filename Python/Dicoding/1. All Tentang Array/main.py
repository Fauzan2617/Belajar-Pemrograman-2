# List in Python

# Deklarasi Array 
# 1. Deklarasi plus nilainya
d = [1,2,3,"halo",1.2]
print(d)
# Deklarasi hanya template saja
template_array = [ 0 for i in range(1-10)]
print(template_array)

# Membuat list dengan for, nilai defaultnya bisa diubah
# Dengan cara memakai for i in
var_arr = [0 for i in range(10)]
for i in range(10):
    var_arr[i] = i
    
print(var_arr)

# Mengetahui penempatan memori pada array/list
# Setiap isi dari array memiliki memori yg berbeda
# for element in a:
#     print(id(element))
    
# Step by Step dari list
list_A = [1,2,3,4,5,6,7,8]

for i in range(len(list_A)):
    index_Awal = list_A[i]
    next_index = i+1
    
    if next_index < len(list_A):
        next_element = list_A[next_index]
    else:
        next_element = None
        
    print("Index Awal{} & index selanjutnya adalah{}".format(index_Awal,next_element))