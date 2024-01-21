package bubblesort;

import java.util.*;

class main {

    public static void main(String[] args) {
        int[] data = { 23, 56, 42, 78, 46 };
        bubblesort(data);

        double[] data2 = { 1.2, 1.6, 3.6, 7.5, 3.2 };
        bubblesortdouble(data2);

    }

    private static void bubblesort(int[] bilangan) {
        // Tampilkan sebelum
        System.out.println("Data sebelum di sort");
        System.err.println(Arrays.toString(bilangan));

        // logic bubblesort
        for (int i = 0; i < bilangan.length; i++) {
            for (int j = 0; j < bilangan.length - 1; j++) {

                if (bilangan[j] < bilangan[j + 1]) {
                    // Maka ditukar
                    int tampung = bilangan[j];
                    bilangan[j] = bilangan[j + 1];
                    bilangan[j + 1] = tampung;
                }
            }
        }

        // Tampilkan sudah di urut
        System.out.println("Datang telah di sort");
        System.out.println(Arrays.toString(bilangan));
    }

    private static void bubblesortdouble(double[] bilangan) {
        // Tampilkan sebelum
        System.out.println("Data sebelum di sort");
        System.out.println(Arrays.toString(bilangan));

        // logic bubblesort
        for (int i = 0; i < bilangan.length; i++) {
            for (int j = 0; j < bilangan.length - 1; j++) {

                if (bilangan[j] > bilangan[j + 1]) {
                    // Maka ditukar
                    double tampung = bilangan[j];
                    bilangan[j] = bilangan[j + 1];
                    bilangan[j + 1] = tampung;
                }
            }
        }

        // Tampilkan sudah di urut
        System.out.println("Datang telah di sort");
        System.out.println(Arrays.toString(bilangan));

    }

}