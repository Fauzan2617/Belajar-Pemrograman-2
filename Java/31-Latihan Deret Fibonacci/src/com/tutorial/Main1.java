package com.tutorial;
import java.util.*;

public class Main1 {
    
    public static void main(String[] args) {
        Scanner user = new Scanner (System.in);
        // Deklarasi
        int f_n,n, f_n_1, f_n_2;

        System.out.println("Masukkan N yang ingin dicari :");
        n = user.nextInt();

        f_n_1 = 1;
        f_n_2 = 0;
        f_n = 1;

        for(int i = 1; i<n; i++){
            System.out.println("Fibonacci ke" + i + "adalah" + f_n );

            f_n = f_n_1 + f_n_2;
            f_n_2 = f_n_1;
            f_n_1 = f_n;
        }

    }
}
