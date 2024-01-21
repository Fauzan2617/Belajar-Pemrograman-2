from time import time
from .util import random_string
from . import Database
import time

def create(penulis,judul,tahun):
    data_template = Database.TEMPLATE.copy()
    
    data_template["pk"] = random_string(5)
    data_template["dateadd"] = time.strftime("%Y-%m-%d-%H-%M-S%z", time.gmtime())
    data_template["judul"] = judul + Database.TEMPLATE["judul"][len(judul):]
    data_template["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):]
    data_template["tahun"] = tahun

    datastr = f'{data_template["pk"]},{data_template["dateadd"]},{data_template["judul"]},{data_template["penulis"]},{data_template["tahun"]}\n'
    
    try:
        with open(Database.DBNAME,'a',encoding="utf-8") as file:
            file.write(datastr)
    except:
        print("Data gagal di buat")



def create_data():
    penulis = input("Penulis :")
    judul = input("Judul: ")
    tahun = input("tahun: ")
    
    data_template = Database.TEMPLATE.copy()
    
    data_template["pk"] = random_string(5)
    data_template["dateadd"] = time.strftime("%Y-%m-%d-%H-%M-S%z", time.gmtime())
    data_template["judul"] = judul + Database.TEMPLATE["judul"][len(judul):]
    data_template["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):]
    data_template["tahun"] = tahun

    datastr = f'{data_template["pk"]},{data_template["dateadd"]},{data_template["judul"]},{data_template["penulis"]},{data_template["tahun"]}\n'
    
    try:
        with open(Database.DBNAME,'w',encoding="utf-8") as file:
            file.write(datastr)
    except:
        print("Data gagal di buat")
        
    
    # Fungsi Read
def read():
    try:
        with open(Database.DBNAME,'r') as file:
            content = file.readlines()
            return content
    except:
        print("gagall banggg")
        return False