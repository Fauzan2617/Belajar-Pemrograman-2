package SelectionSorting;

import java.net.Socket;
import java.util.Arrays;

public class main {
    
    public static void main(String[] args) {
        int[] data = {23,45,12,56,89};
        selectionsortINT(data);

        double[] data2 = {1.2,4.3,2.4,3.4};
        selectionsortDouble(data2);
    }

    private static void selectionsortINT(int [] bilangan){
        //Sebelum Sort
        System.out.println("===SEBELUM DIUBAH===");
        System.out.println(Arrays.toString(bilangan));

        //Logic nya
        for(int i = 0; i<bilangan.length; i++){
            int index = i;
            for(int j = i; j<bilangan.length; j++){

                if(bilangan[index] < bilangan[j]){
                    index = j;
                }
            }
            int tampungan = bilangan[i];
            bilangan[i] = bilangan[index];
            bilangan[index] = tampungan;
        }


        // Setelah Sort
        System.out.println("===SESUDAH DIUBAH===");
        System.out.println(Arrays.toString(bilangan));
        System.out.println("\n\n");
    }



    private static void selectionsortDouble(double [] bilangan){
        //Sebelum Sort
        System.out.println("===SEBELUM DIUBAH===");
        System.out.println(Arrays.toString(bilangan));

        //Logic nya
        for(int i = 0; i<bilangan.length; i++){
            int index = i;
            for(int j = i; j<bilangan.length; j++){

                if(bilangan[index] < bilangan[j]){
                    index = j;
                }
            }
            double tampungan = bilangan[i];
            bilangan[i] = bilangan[index];
            bilangan[index] = tampungan;
        }


        // Setelah Sort
        System.out.println("===SESUDAH DIUBAH===");
        System.out.println(Arrays.toString(bilangan));
    }

}
