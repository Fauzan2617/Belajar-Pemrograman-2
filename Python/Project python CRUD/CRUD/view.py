from . import Operasi
from . import database
import time
from .util import random_string



def create_console():
    print("\n\n"+"="*100)
    penulis = input("Penulis: ")
    judul = input("Judul: ")
    
    while(True):
        try:
            tahun = int(input("Tahun: "))
            if len(str(tahun)) == 4:
                break
            else:
                print("Tahun harus dimasukkan dalam angka, tahun (yyyy)")
        except:
            print("Tahun harus dimasukkan dalam angka, tahun (yyyy)")

    Operasi.create(penulis,judul,tahun)
    print("Ini adalah data baru anda")
    read_console()





def read_console():
    data_file = Operasi.read()
    
    index = "No"
    judul = "Judul"
    penulis = "Penulis"
    tahun = "Tahun"

    # Header
    print("\n"+"="*100)
    print(f"{index:4} | {judul:40} | {penulis:40} | {tahun:5}")
    print("-"*100)
    
    # Data
    for index,data in enumerate(data_file):
        data_break = data.split(",")
        pk = data_break[0]
        date_add = data_break[1]
        penulis = data_break[2]
        judul = data_break[3]
        tahun = data_break[4]
        print(f"{index+1:4} | {judul:.40} | {penulis:.40} | {tahun:4}",end="")

    # Footer
    print("="*100+"\n")