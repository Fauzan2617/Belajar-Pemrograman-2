import os
import CRUD as CRUD

if __name__ == "__main__":
    sistem_operasi = os.name
    
    while(True):
        match sistem_operasi:
            case "nt": os.system("cls")
        
        print("SELAMAT DATANG DI PROGRAM")
        print("DATABASES PERPUSTAKAAN BUKU")
        print("="*100)
    
        # Ngecek Databases
        CRUD.checkdatabase()
    
        print("1. Read Data")
        print("2. Create Data")
        print("3. Detele Data")
        print("4. Update Data\n")
    
        user_option = input("Masukkan Data: ")
    
        match user_option:
            case "1" : CRUD.read_console()
            case "2" : CRUD.create_console()
            case "3" : print("Delete Data")
            case "4" : print("Update data")
        
        is_done = input("Sudah Selesai ? (y/n)")
        if is_done == "y" or is_done == "Y":
            break

    print("PROGRAM SUDAH SELESAI TERIMA KASIH KAKAKK")