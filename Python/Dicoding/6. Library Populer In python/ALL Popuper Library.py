'''
LIBRARY RE (Reguler Expression)
'''
import re

a = "Halogaisss"
b = '^H........s$'

hasil = re.match(b,a)

if hasil:
    print("Berhasil Ditemukan")
else:
    print("Gagal ditemukan")
    
    
    
    
'''
LIBRARY Math (Matematika)
'''
import math

Akar = math.sqrt(10)
print (Akar)




'''
LIBRARY Parser
import Getopt atau ArgParse
'''
import argparse
 
parser = argparse.ArgumentParser()
parser.add_argument('-o', '--output', action='store_true', help="tampilkan output")
args = parser.parse_args()
 
if args.output:
   print("Halo, ini merupakan sebuah output dari panggildicoding.py")
   
   
   
   
   
'''
LIBRARY Pengolahan Data
'''
# 1. Pandas
# import pandas as pd # type: ignore

# dict = {
#     'nama' : ['fauzan','dwi','putera'],
#     'kelas': ['10','15','20'],
# }

# excel = pd.DataFrame(dict)
# print(dict)

# 2. Matholib
# import matplotlib.pyplot as plt
 
# # Data
# x = [1, 2, 3, 4, 5]
# y = [2, 4, 6, 8, 10]
 
# # Membuat plot garis
# plt.plot(x, y)
 
# # Menambahkan judul dan label sumbu
# plt.title("Contoh Plot Garis")
# plt.xlabel("Sumbu X")
# plt.ylabel("Sumbu Y")
 
# # Menampilkan plot
# plt.show()




'''
LIBRARY File Management
'''
# 1. Jsoimport json
import json
# contoh JSON:
x = '{ "nama":"Buchori", "umur":22, "Kota":"New York"}'
 
# parse  x:
y = json.loads(x)
 
print(y["umur"])

# 2. Pickle
# Contoh menyimpan objek jadi file
import pickle
contoh_dictionary = {1:"6", 2:"2", 3:"f"}
pickle_keluar = open("dict.pickle","wb")
pickle.dump(contoh_dictionary, pickle_keluar)
pickle_keluar.close()

# Contoh Mengextra pickle dan menaruh pada variable
import pickle
pickle_masuk = open("dict.pickle", "rb")
contohDictionary = pickle.load(pickle_masuk)
pickle_masuk.close()
 
print(contohDictionary)



'''
LIBRARY Web Scripping
'''
# 1. Beautifulsoup
from urllib.request import urlopen
from bs4 import BeautifulSoup
 
# Pengambilan konten
url = "http://python.org/"
page = urlopen(url)
html = page.read().decode("utf-8")
 
# Membuat objek BeautifulSoup
soup = BeautifulSoup(html, "html.parser")
 
# Mencetak judul halaman
print(soup.title)

# 2. Urllib
from urllib.request import urlopen
 
# Pengambilan konten
url = "http://python.org/"
page = urlopen(url)
html = page.read().decode("utf-8")
 
# Mencari indeks awal dan akhir
start_index = html.find("<title>") + len("<title>")
end_index = html.find("</title>")
 
# Mengekstrak dan mencetak judul halaman
title = html[start_index:end_index]
print(title)


