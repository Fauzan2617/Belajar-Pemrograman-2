package InsertionSort;

import java.util.Arrays;

import javax.sound.midi.Soundbank;

public class main {

    public static void main(String[] args) {
        int[] nilai = { 90, 56, 34, 24, 56 };
        InsertionSort(nilai);

    }

    private static void InsertionSort(int[] bilangan) {
        System.out.println("==DATA SEBELUM==");
        System.out.println(Arrays.toString(bilangan));
        // Data dimulai dari index ke 1 dibandingkan dgn data ke 0 
        // ketika tidak memenuhi syarat maka akan bertambah satu index nya 
        // dan jika misalkan memenuhi syarat maka ditukar dan dikurang satu index nya ke kiri
        // dikurang hingga ke index 0 misalkan memenuhi syarat. misalkan tidak ditambah lagi satu
        // dan misalkan sudah hingga kek index 0 akan langsung membandingkan ke index terakhir
        System.out.println("UNTUK MEMAKAI WHILE");
        for(int i = 1; i < bilangan.length; i++){
            int j = i;

            while (j > 0) {
                if(bilangan[j] < bilangan[j-1]){

                    int tampungan1 = bilangan[j];
                    bilangan[j] = bilangan[j-1];
                    bilangan[j-1] = tampungan1;
                }
                j--;
            }
        }
        System.out.println("Data sudah pakai while");
        System.out.println(Arrays.toString(bilangan));

        System.out.println("UNTUK MEMAKAI FOR");
        for (int i = 1; i < bilangan.length; i++) {

            for (int j = i; j > 0; j--) {
                if (bilangan[j] < bilangan[j - 1]) {

                    int tampungan = bilangan[j];
                    bilangan[j] = bilangan[j - 1];
                    bilangan[j - 1] = tampungan;
                }
            }

        }
        System.out.println("Data sesudah pakai for");
        System.out.println(Arrays.toString(bilangan));
    }
}
