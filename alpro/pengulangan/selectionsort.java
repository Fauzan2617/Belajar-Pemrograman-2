package pengulangan;

import java.util.Arrays;
import java.util.Scanner;

public class selectionsort {

    public static void main(String[] args) {

        // Inisialisasi array
        int[] data = new int[5];

        // Tambahkan fungsi untuk menginput angka
        Scanner sc = new Scanner(System.in);
        for (int i = 0; i < data.length; i++) {
            System.out.print("Masukkan angka ke-" + (i + 1) + ": ");
            data[i] = sc.nextInt();
        }

        // Tampilkan data sebelum diurut
        System.out.println("Data sebelum diurut:");
        System.out.println(Arrays.toString(data));

        // Urutkan data menggunakan algoritma selection sort
        selectionSort(data);

        // Tampilkan data setelah diurut
        System.out.println("Data setelah diurut:");
        System.out.println(Arrays.toString(data));
    }

    private static void selectionSort(int[] data) {
        // Iterasi sebanyak panjang array - 1
        for (int i = 0; i < data.length - 1; i++) {
            // Cari indeks data terkecil dari data[i] ke data[data.length - 1]
            int minIndex = i;
            for (int j = i + 1; j < data.length; j++) {
                if (data[j] < data[minIndex]) {
                    minIndex = j;
                }
            }

            // Jika indeks data terkecil bukan i, maka lakukan swap
            if (minIndex != i) {
                int temp = data[i];
                data[i] = data[minIndex];
                data[minIndex] = temp;
            }
        }
    }
}
