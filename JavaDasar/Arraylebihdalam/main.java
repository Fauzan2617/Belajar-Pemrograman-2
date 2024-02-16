package Arraylebihdalam;

import java.util.*;

public class main {

    public static void main(String[] args) {
        int[] Arrayangka = {1,2,3,4,5};
        int[] Arrayangka1 = {6,7,8,56};

        System.out.println(Arrays.toString(Arrayangka));
        System.out.println(Arrays.toString(Arrayangka1));

        // Kedua memori akan sama ketika keduanya gabung
        // Sehingga ketika ada perubahan pada satu array,yg terjadi akan merubah keduanya
        Arrayangka = Arrayangka1;
        Arrayangka[1] = 10;
        Arrayangka1[3] = 50;
        System.out.println(Arrays.toString(Arrayangka));
        System.out.println(Arrays.toString(Arrayangka1));

        ubaharray(Arrayangka1);
        System.out.println(Arrays.toString(Arrayangka));
        System.out.println(Arrays.toString(Arrayangka1));

    }

    // Method yang argumentnya pass by refrence
    // Bukan pass by value
    private static void ubaharray(int[] dataaaray){
        dataaaray[2 ] = 150;
        }
}