package Node;
public class LinkedList {
	    node head;

	    void tambahDiAwal(double data) {
	        node newNode = new node(data);
	        newNode.next = head;
	        head = newNode;
	    }

	    void tambahDiAkhir(double data) {
	        node newNode = new node(data);
	        if (head == null) {
	            head = newNode;
	            return;
	        }

	        node last = head;
	        while (last.next != null) {
	            last = last.next;
	        }
	        last.next = newNode;
	    }

	    void tambahDiTengah(double data, int posisi) {
	        node newNode = new node(data);
	        if (posisi == 0) {
	            newNode.next = head;
	            head = newNode;
	            return;
	        }

	        node current = head;
	        for (int i = 0; i < posisi - 1 && current != null; i++) {
	            current = current.next;
	        }

	        if (current == null) {
	            System.out.println("Posisi tidak valid");
	            return;
	        }

	        newNode.next = current.next;
	        current.next = newNode;
	    }

	    void tampilkan() {
	        node current = head;
	        while (current != null) {
	            System.out.print((int) current.data + " ");
	            current = current.next; // Maju ke node berikutnya
	        }
	        System.out.println();
	    }

}