package bubblesort;

import java.util.Arrays;

public class main2 {

    public static void main(String[] args) {

        int[] arraydata = { 23, 45, 23, 17, 78, 43 };
        System.out.println("Data yang belum di sort" + Arrays.toString(arraydata));
        // Bubble Sort
        for (int i = 0; i < arraydata.length-1; i++) {
            for (int j = 0; j < arraydata.length-1; j++) {
                if (arraydata[j] > arraydata[j + 1]) {

                    int tampungan = arraydata[j];
                    arraydata[j] = arraydata[j + 1];
                    arraydata[j + 1] = tampungan;
                }
            }
        }
        System.out.println("Data yang sudah di sort" + Arrays.toString(
        arraydata));

    }
}
