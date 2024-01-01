package pengulangan;
import java.util.Arrays;
import java.util.Scanner;

public class ArrInteger {

    public static void main(String[] args) {

        // Inisialisasi array
        int[] data = new int[7];

        // Tambahkan fungsi untuk menginput angka
        Scanner sc = new Scanner(System.in);
        for (int i = 0; i < data.length; i++) {
            System.out.print("Masukkan angka ke-" + (i + 1) + ": ");
            data[i] = sc.nextInt();
        }

        // Tampilkan data sebelum diurut
        System.out.println("Data sebelum diurut:");
        System.out.println(Arrays.toString(data));

        // Urutkan data menggunakan algoritma bubble sort
        bubbleSort(data);

        // Tampilkan data setelah diurut
        System.out.println("Data setelah diurut:");
        System.out.println(Arrays.toString(data));
    }

    private static void bubbleSort(int[] data) {
        // Iterasi sebanyak panjang array - 1
        for (int i = 0; i < data.length - 1; i++) {
            // Iterasi dari awal array sampai akhir array - i
            for (int j = 0; j < data.length - i - 1; j++) {
                // Jika data di indeks j lebih besar dari data di indeks j + 1, maka lakukan swap
                if (data[j] > data[j + 1]) {
                    int temp = data[j];
                    data[j] = data[j + 1];
                    data[j + 1] = temp;
                }
            }
        }
    }
}