package Node;

public class main {
public static void main(String[] args) {
	
	        LinkedList list = new LinkedList();
	        list.tambahDiAwal(3);
            list.tambahDiAkhir(7); 
	        list.tambahDiAkhir(6); 
            list.tambahDiTengah(8,1);
	        list.tambahDiAwal(9);
	        // menampilkan hasil dari linkedlist yang sudah di tambahkan
	        // di atas tadi
	        System.out.print("Elemen list: ");
	        list.tampilkan();
	    }
	
}