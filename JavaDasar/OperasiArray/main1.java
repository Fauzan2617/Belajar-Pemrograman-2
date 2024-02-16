package OperasiArray;

import java.util.Arrays;

public class main1 {
    
    public static void main(String[] args) {
        

        int[] a = {1,2,3,4,5};
        int[] b = new int [5];

    // Copy Array dengan for
    for(int i =0;i<a.length;i++){
        b[i] = a[i]; 
    }
    printArray(b);
    printArray(a);

    // Copy Array dengan fitur Copy Of
    System.out.println("Copy dengan copyof");   
    
    int c[] = Arrays.copyOf(a, 5);
    printArray(c);

    // Copy menggunakan fitur copy of range
    System.out.println("Copy dengan Copy Of Range");
    int d[] = Arrays.copyOfRange(a, 1, 5);
    printArray(d);

    // Menggunakan fitur fill
    System.out.println("Fitur Fill");
    int[] e = new int[5];
    Arrays.fill(e, 10);
    printArray(e);








    }
    private static void printArray(int[] data){
        System.out.println("Print Arays" + Arrays.toString(data));
    }
}
