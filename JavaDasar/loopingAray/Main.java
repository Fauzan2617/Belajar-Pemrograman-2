// LOOPING DENGAN ARRAY
package loopingAray;

public  class Main {

    public static void main(String[] args) {

        int [] arrayAngka = {11,12,13,14,15,16,17,18};

        // Looping standart
        for(int i = 0; i<8;i++){
            System.out.println("Index ke " + i + "datanya adalah" + arrayAngka[i]);
        }

        // Looping dengan Length
         for(int i = 0; i <arrayAngka.length; i++){
            System.out.println("Index ke " + i + "datanya adalah" + arrayAngka[i]);
        }

        // loopinh khusus untunk coleection
        // Looping for each digunakan ketika tidak menggunakan index
        System.out.println("Looping for each");
        for(int angka : arrayAngka){
            System.out.println(angka);

        // L
        }

    }
}