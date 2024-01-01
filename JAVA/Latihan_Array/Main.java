package Latihan_Array;
import java.util.*;

public class Main {
    
    public static void main(String[] args) {
    int[] arrayAngka1 = {1,2,3,4,5,6,7};
    int [] arrayAngka2 = {3,2,5,2,5,6,8};

    // PENJUMLAHAN DUA BUAH ARRAY
    int[] hasil = tambaharray(arrayAngka1, arrayAngka2);
    printArray(hasil);

    // MENGGABUNGKAN DUA BUAH ARRAY
    int[] arrayhasil3 = new int [arrayAngka1.length + arrayAngka2.length]; 
    
    for(int i=0;i<arrayAngka1.length;i++){
        arrayhasil3[i] = arrayAngka1[i];
    }

    for(int i =0;i<arrayAngka2.length;i++){
        arrayhasil3[i + arrayAngka1.length] = arrayAngka2[i];
    }

    printArray(arrayhasil3);


    // SORTING REVERSE
    int[] araybuffer = Arrays.copyOf(arrayAngka2, arrayAngka2.length);

    Arrays.sort(arrayAngka1);
    for(int i =0;i<arrayAngka1.length;i++){
        arrayAngka1[i] = araybuffer[(araybuffer.length-1)-i];
    }
    printArray(arrayAngka1);



    }
    private static int[] tambaharray(int[] arrayint1 , int[] arrayint2){
    int[] hasil = new int[arrayint1.length];
    for(int i = 0;i<arrayint1.length;i++){
    hasil[i] = arrayint1[i] + arrayint2 [i];
    }
    return hasil;
    
    }




    private static void printArray(int[]dataaaray){
        System.out.println(Arrays.toString(dataaaray));
    }
}
