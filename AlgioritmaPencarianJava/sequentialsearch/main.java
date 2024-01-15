package sequentialsearch;

import java.util.*;

public class main {

    public static void main(String[] args) {
        int[] data = { 1, 2, 3, 4, 5, 6, 7 };
        sequentialsearch(data);

    }

    public static void sequentialsearch(int[] bilangan) {
        // Sequential search berguna untuk mencari data yang ingin kita cari
        // ketika ditemukan maka menunjukkan lokasi index dan datanya
        Scanner inputuser = new Scanner(System.in);
        System.out.print("Masukkan data yang ingin anda cari :");
        int key = inputuser.nextInt();

        boolean status = false;
        for (int i = 0; i < bilangan.length - 1; i++) {
            if (bilangan[i] == key) {
                System.out.println(key + "\tBilangan yang anda cari ada di index:" + i);
                status = true;
                break;
            }
        }
        if (status == false) {
            System.out.println("Data yang anda cari tidak ditemukan");
        }
    }

}
