package InsertionSort;

import java.util.Arrays;

public class main1 {
    
    public static void main(String[] args) {
        
        int[] datab = {23,45,34,89,12,90,34};
        System.out.println("Data yang belum di sort" + Arrays.toString(datab));

        
        // Indsertion Sort 
        for(int i = 1; i<datab.length;i++){
            for(int j = i; j > 0; j--){
                if(datab[j] > datab[j-1]){

                    int tampung = datab[j-1];
                    datab[j-1] = datab[j];
                    datab[j] = tampung;
                }
            }
        }
        System.out.println("Data yang sudah di sorting" + Arrays.toString(datab));
    }
}
