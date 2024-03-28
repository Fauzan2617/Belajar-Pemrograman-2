a = [10,200,23,58,20]
left = a[0]

for i in range(1,len(a)):
    right = a[i]
    
    if right > left:
        left = right
        
print (left)

var_array = [i for i in range(101)]
for i in var_array:
  total =+ i
jumlah_elemen = len(var_array)
if jumlah_elemen != 0:
  result = total/jumlah_elemen
else:
  result = 0
print(result)