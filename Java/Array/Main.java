package Array;

import java.util.Arrays;

public class Main {
    
    public static void main(String[] args) {

    // ASSIGNMENT ARRAY
    // Tipedata [] nama = {komponen-komponen}
    //               index 0 1 2 3
    int [] arrayInteger = {1,2,3,4};
    System.out.println(arrayInteger[1]);


    // DEKLARASI ARRAY
    // tipedata [] nama = new int [jumlahArray]
    float[] data_float = new float[5];
    data_float [1] = 11;

    System.out.println(data_float[1]);

    System.out.println(Arrays.toString(data_float));
    System.out.println(Arrays.toString(arrayInteger));
    


    }
}
