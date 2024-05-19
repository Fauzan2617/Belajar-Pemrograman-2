from . import operasi


DBNAME = "data.txt"
TEMPLATE = {
    "pk":"XXXXXX",
    "dateadd":"yyyy-mm-dd",
    "judul":255*" ",
    "penulis":255*" ",
    "tahun":"yyyy-mm-dd"
}

def checkdatabase():
    try:
        with open(DBNAME,"r") as file:
            print("Databases di temukan")
    except:
            print("Database tidak ditemukan")
            operasi.create_data()