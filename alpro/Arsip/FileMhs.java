package Arsip;

import java.io.BufferedReader;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.ObjectOutputStream;
import java.util.Scanner;

public class FileMhs {
    
    void SaveFIleMhs() {
            Mahasiswa Mhs=new Mahasiswa();
            int no;
            String nama;
            float ip;
        
            ObjectOutputStream out = null;
            try {
                out=new ObjectOutputStream(new FileOutputStream
                        ("c:\\diaz\\Nasabah.dat"+ ""));
                for (int i=1;i<=3;i++) {
                    Scanner sc= new Scanner(System.in);
                    System.out.print("No: "); no=sc.nextInt();
                    System.out.print("Nama: "); nama=sc.next();
                    System.out.print("IPk : "); ip=sc.nextFloat();
                    Mhs=new Mahasiswa(no,nama,ip);
                    out.writeObject(Mhs);
                }
            out.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
        
    
    void BacaFileMhs() {
        
    }
    public static void main(String[] args) {
        FileMhs F=new FileMhs();
        F.SaveFIleMhs();
        F.BacaFileMhs();
    }
}