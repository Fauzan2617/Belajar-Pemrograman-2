package ARRAY;
	
	import java.util.Scanner;
	
public class BilBulat {
	
	    public static void main(String[] args) {
	        // Membuat array dengan panjang lima elemen
	        int[] array = new int[5];

	        // Membaca input nilai setiap elemen dari keyboard
	        Scanner input = new Scanner(System.in);
	        for (int i = 0; i < 5; i++) {
	            System.out.print("Masukkan angka: ");
	            array[i] = input.nextInt();
	        }

	        // Menampilkan nilai setiap elemen
	        System.out.println("Nilai setiap elemen dalam array:");
	        for (int i = 0; i < 5; i++) {
	            System.out.println("Elemen ke-" + (i+1) + ": " + array[i]);
	        }
	    }
	}



