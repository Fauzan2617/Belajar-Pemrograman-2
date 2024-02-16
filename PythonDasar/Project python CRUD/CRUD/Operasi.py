from time import time
from . import database
from .util import random_string
import time

# FUNGSI MENAMBAHKAN DATA KE DATABASE
def create(penulis,judul,tahun):
    data = database.TEMPLATE.copy()

    data["pk"] = random_string(6)
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z",time.gmtime())
    data["penulis"] = penulis + database.TEMPLATE["penulis"][len(penulis):]
    data["judul"] = judul + database.TEMPLATE["judul"][len(judul):]
    data["tahun"] = str(tahun)
    
    data_str = f'{data["pk"]},{data["date_add"]},{data["penulis"]},{data["judul"]},{data["tahun"]}\n'
    try:
        with open(database.DB_NAME,'a',encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("Udah Gagal cokk ditambahkan")


# FUNGSI MEMBUAT DATA PERTAMA DALAM DATABASE
def create_first_data():
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

    data = database.TEMPLATE.copy()

    data["pk"] = random_string(6)
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z",time.gmtime())
    data["penulis"] = penulis + database.TEMPLATE["penulis"][len(penulis):]
    data["judul"] = judul + database.TEMPLATE["judul"][len(judul):]
    data["tahun"] = tahun

    data_str = f'{data["pk"]},{data["date_add"]},{data["penulis"]},{data["judul"]},{data["tahun"]}\n'
    try:
        with open(database.DB_NAME,'w',encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("Udah lah Gagal booooos")

def read():
    try:
        with open(database.DB_NAME, 'r') as file:
            content = file.readlines()
            return content
    except:
        print("Membaca database error")
        return False
    