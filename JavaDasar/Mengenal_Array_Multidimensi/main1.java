package Mengenal_Array_Multidimensi;
import java.util.*;


public class main1 {
    
    public static void main(String[] args) {
        // Matrix dengan deklarasi
        int[][] array2D = new int[3][5];
        
        // Matrix menggunakan Isi langsung
        int[][] array2D1 = {{1,2,3,4,5},{1,2,3,4,5}};
        look(array2D1);
        look(array2D);


        // Menampilkan Matrix menggunakan DeepToSrtring
        System.err.println(Arrays.deepToString(array2D));




    }

    private static void look(int[][] arraylook){
        // Menampilkan array menggunakan for
        //   for(int i=0;i<arraylook.length;i++){
        //     System.out.print("[");
        //     for(int j=0;j<arraylook[i].length;j++){
        //         System.out.print(arraylook[i][j]+',');
        //     }
        //     System.out.print(']'+ '\n');
        // }
        
        // Menampilkan array menggunakan for each
        for(int[] baris:arraylook){
            System.out.print("[");
            for(int kolom : baris){
                System.out.print(kolom + ',');
            }
            System.out.print("]");
        }


    }
}
