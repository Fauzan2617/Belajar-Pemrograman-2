package InsertionSort;

import java.util.Arrays;

public class main {

    public static void main(String[] args) {
        int[] nilai = { 90, 56, 34, 24, 56 };
        InsertionSort(nilai);

    }

    private static void InsertionSort(int[] bilangan) {
        System.out.println("==DATA SEBELUM==");
        System.out.println(Arrays.toString(bilangan));

        for (int i = 1; i < bilangan.length; i++) {

            for (int j = i; j > 0; j--) {
                if (bilangan[j] < bilangan[j - 1]) {

                    int tampungan = bilangan[j];
                    bilangan[j] = bilangan[j - 1];
                    bilangan[j - 1] = tampungan;
                }
            }

        }

        System.out.println("==DATA SESUDAH==");
        System.out.println(Arrays.toString(bilangan));
    }
}
