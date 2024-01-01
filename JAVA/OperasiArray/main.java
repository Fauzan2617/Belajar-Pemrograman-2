package OperasiArray;

import java.util.Arrays;

public class main {
    
    public static void main(String[] args) {
    
    int[] Arrayangka1 = {1,2,3,4,5};

    // MERUBAH ARRAY KE STRING
    System.out.println("\nMerubah Array ke dalam String");
    int[] Arrayangka2 = new int[5];

    // MENGKOPI ARRAY DENGAN LOOP
    System.out.println("\nMengkopi dengan loop yang benar\n");
    for(int i = 0; i < Arrayangka1.length;i++){
        Arrayangka2[i] = Arrayangka1[i];
    }
    printArray(Arrayangka2);

    // MENGKOPI ARRAY MENGGUNAKAN COPY OF
    System.out.println("\nMengkopi menggunaka Copy Of");
    int[] Arrayangka3 = Arrays.copyOf(Arrayangka1, 5);
    printArray(Arrayangka3);
    System.out.println(Arrayangka3);
    System.out.println(Arrayangka1);

    // kofi dengan CopyOFRange
    System.out.println("\nMengkofi dengan Copyofrange");
    int[] Arrayangka4 = Arrays.copyOfRange(Arrayangka3, 2, 5);
    printArray(Arrayangka4);
    System.out.println(Arrayangka1);
    System.out.println(Arrayangka4 + "\n");

    // Fiil Array
    // Isi Array akan full dengan angka berdasarkan Val
    System.out.println("\nCopy dengan menggunakan Fill");
    int[] arrayAngka5 = new int[5];
    Arrays.fill(arrayAngka5, 10);
    printArray(arrayAngka5);

    // Komparasi Array
    System.out.println("\nKomparasi Array");
    int[] arrayAngka6 = {5,2,3,4,5,6};
    int[] arrayAngka7 = {1,2,3,4,5,6};

    System.out.println("MEMBANDINGKAN DUA ARRAY DENGAN FITUR equals");
    System.out.println( Arrays.equals(arrayAngka6, arrayAngka7));

    if (Arrays.equals(arrayAngka6, arrayAngka7)) {
        System.out.println("Array ini sama");
    }else{
        System.out.println("Array ini tidak sama");
    }

    System.out.println("\nMengecek Mana Array yang lebih besar");
    System.out.println(Arrays.compare(arrayAngka6, arrayAngka7));
    
    System.out.println("\n Ngecek index yang berbeda");
    System.out.println("Ngecek index yg berbeda\t"+ Arrays.mismatch(arrayAngka6,arrayAngka7));
    
    // Search Array
    int[] arrayAngka8 = {4,5,2,7,5,9,2,3};
    System.out.println("\nSort Array");
    Arrays.sort(arrayAngka8);
    printArray(arrayAngka8);

    // Searching Array
    System.out.println("\nSearch Array");
    int angka = 4;
    int posisi = Arrays.binarySearch(arrayAngka8, angka);
    System.out.println("Posisi" + angka + "Ada di" + posisi);

    }

    private static void printArray( int [ ] dataaaray){
        System.out.println("Isi data" + Arrays.toString(dataaaray));
    }
}
