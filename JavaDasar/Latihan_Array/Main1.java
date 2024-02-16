package Latihan_Array;
import java.util.Arrays;

public class Main1 {
    
    public static void main(String[] args) {
        

        int[] a = {1,2,3,4,5};
        int[] b = {6,7,8,9,10};

        // Menjumlahkan kedua Array
        System.out.println("Menjumlahkan Kedua Array");
        penjumlahan(a,b);

        // Menggabungkan kedua Arrays
        int[] gabungan = new int[a.length + b.length];
        
        for(int i = 0 ; i < a.length ; i++){
            gabungan[i] = a[i] ; 
        }

        for(int i = 0 ; i< b.length;i++){
            gabungan[a.length + i] = b[i];
        }
        printArray(gabungan);


    }

    private static void penjumlahan(int[] data1,int[] data2 ){
        int[] hasil = new int[data2.length];
        for(int i = 0; i<data1.length; i++){
            hasil[i] = data1[i] + data2[i];
        }
        printArray(hasil);
    }

    private static void printArray(int[] data){
        System.out.println("Print Array" + Arrays.toString(data));
    }

}
