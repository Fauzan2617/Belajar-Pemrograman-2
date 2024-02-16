from . import operasi

def create_console():
    penulis = input("Masukkan Penulis :")
    judul = input("Judul :")
    
    while(True):
        try:
            tahun = int(input("Masukkan Tahun :"))
            if len(str(tahun)) == 4:
                break
            else:
                print("Tahun harus dalam bentuk angka, dan formatnya (yyyy)")

        except:
            print("Tahun harus dalam bentuk angka, dan formatnya (yyyy)")
            
    operasi.create(penulis,judul,tahun)
    print("Ini adalah data anda !!")
    read_console()




def read_console():
    data_file = operasi.read()
    
    index = "No"
    judul = "judul"
    penulis = "penulis"
    tahun = "tahun"

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