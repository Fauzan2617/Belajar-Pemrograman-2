package Arsip;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class ArsipUrutan {
	
   public static void main(String[] args) {
      List<String> archive = new ArrayList<>();
      archive.add("Surat A");
      archive.add("Surat j");
      archive.add("Surat B");
      archive.add("Surat a");

      // Mengurutkan arsip berdasarkan urutan abjad
      Collections.sort(archive);

      // Menampilkan arsip yang sudah diurutkan
      for (String surat : archive) {
         System.out.println(surat);
      }
   }
}
