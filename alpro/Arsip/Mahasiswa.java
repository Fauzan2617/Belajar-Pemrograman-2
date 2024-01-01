package Arsip;

import java.util.Scanner;

public class Mahasiswa implements java.io.Serializable {
    int nim;
    String nama;
    float ipk;
    
    Mahasiswa(){
        
    }
    
    Mahasiswa(int mynim, String mynama, float myip) {
        nim=mynim;
        nama=mynama;
        ipk=myip;
    }
    
    
    void BacaMahasiswa() {
        Scanner sc=new Scanner(System.in);
        System.out.println("nim: "); nim=sc.nextInt();
        System.out.println("nama: "); nama=sc.next();
        System.out.println("ipk: "); ipk=sc.nextFloat();
    }
    
    void TampilMahasiswa() {
        System.out.println("Data: "
                +nim+","+nama+","+ipk);
    }
}