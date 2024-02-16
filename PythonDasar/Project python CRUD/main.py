import os
import CRUD as CRUD


if __name__ == "__main__":
    sistem_operasi = os.name
    
    while(True):
        match sistem_operasi:
            case "nt": os.system("cls")
        
        print("SELAMAT DATANG DI PROGRAM")
        print("DATABASES PERPUS")
        print("============================")
        
        # Ngecek database
        CRUD.init_console()
        
        
        print("1. Read Data")
        print("2. Create Data")
        print("3. Update Data ")
        print("4. Delete Data\n")

        user_option = input("Masukkan Opsi: ")
        
        match user_option:
            case "1": CRUD.read_console()
            case "2": CRUD.create_console()
            case "3": print("Update Data")
            case "4": print("Delete Data")
            
        
        is_done = input("Apakah sudah selesai (y/n) ?")
        if is_done == "y" or is_done == "Y":
            break
        
    print("Programm Berakhirr Terima Kasihh kakakk")