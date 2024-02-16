package Mengenal_Array_Multidimensi;

import java.util.Arrays;

public class main {

    public static void main(String[] args) {
        System.out.println("BELAJAR ARRAY MULTI DIMENSI");

        // Cara Membuat Array 2 dimensi
        int[][] array2D = {
                { 1, 2 },
                { 1, 2 }
        };
        viewarray2D(array2D);
        // Cara menampilkan Array2D menggunakan deeptostring
        // System.out.print(Arrays.deepToString(array2D));

        // Membuat Array 2 dimensi/Matrix dengan deklarasi
        // int[baris][kolom]
        int[][] array2D2 = new int[3][5];
        viewarray2D(array2D2);

        // Array java tidak harus sama antara baris dan kolom
        int[][] array2D3 = {
                { 1, 2, 3, 4 },
                { 4, 5 },
                { 4, 2, 3 }
        };
        viewarray2D(array2D3);

    }

    private static void viewarray1D(int[][] view) {
        System.out.println(Arrays.toString(view));
    }

    private static void viewarray2D(int[][] view) {        // MENAMPILKAN MENGGUNAKAN 2D FOR
        // for(int i = 0 ; i < array2D2.length; i++){
        // System.out.print("[");
        // for(int k = 0; k < array2D2[i].length; k++){
        // System.out.print(array2D2[i][k] + ',');
        // }
        // System.out.print("]\n");
        // }

        for(int i = 0;i< viewarray2D.length;i++){
            System.out.print("[");
            for(int j = 0;j<viewarray2D[1].length;j++){

            }
        }

        // MENAMPILKKAN MENGGUNAKAN 2D FOREACH
        for (int[] baris : view) {
            System.out.print("[");
            for (int angka : baris) {
                System.out.print(angka + ",");
            }
            System.out.print("]\n");
        }
    }

}
