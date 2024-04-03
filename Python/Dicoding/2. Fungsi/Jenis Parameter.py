# Parameter
'''
1. Positional & Keyword
Parameter yang menerima jenis Argument Positional & Keyword
'''
def luas_lingkaran(phi,r):
    result = phi * r * r
    return result

print(luas_lingkaran(3.14,7))
print(luas_lingkaran(phi= 3.14, r= 7))


'''
2. Positional Only
Parameter yang hanya menerima argument positional dgn tanda "/"
'''
def luas_lingkaran(phi,r,/):
    result = phi * r * r
    return result

print(luas_lingkaran(3.14,7))

'''
3. Keyword Only
Parameter yang hanya menerima Argument Keyword dgn tanda "*"
'''
def luas_lingkaran(*,phi,r):
    result = phi * r * r
    return result

print(luas_lingkaran(phi= 3.14, r= 7))

'''
4. Var-positional
Parameter yang menerima argument variasi dgn tanda *args
Semua argument akan diubah ke dalam Tuple
'''
def luas_lingkaran(*args):
    result = sum(args)
    return result

print(luas_lingkaran(3.14, 7))

'''
5. Var-Keyword
Parameter yang menerima argument variasi dgn tanda **kwargs
Semua argument akan berubah jadi dictionary
Argument sbg (Value) & Identifier sbg (Key)
'''
def luas_lingkaran(**kwargs):
    info = ""
    for key,value in kwargs.items():
        info += key + value + ","
    return info

print(luas_lingkaran(phis= "3.14", r= "7"))