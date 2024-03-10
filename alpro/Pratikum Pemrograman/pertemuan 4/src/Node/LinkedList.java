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

		void hapusMid(int e)
    {
        node preNode = new node(0);
        node tempNode;
        int i;
        boolean ketemu;
        
        if(head == null)
        {
            System.out.println("Elemen List Kosong");
        }
        else
        {
            ketemu = false;
            i = 1;
            tempNode = head;
            while (tempNode.getNext() != null && !ketemu)
            {
                if(tempNode.getNilai() == e)
                {
                    ketemu = true;
                }
                else
                {
                    preNode = tempNode;
                    tempNode = tempNode.getNext();
                    i++;
                }
            }
            if(ketemu == true)
            {
                if (i == 1)
                    head = null;
                else
                {
                    preNode.setNext(tempNode.getNext());
                }
            }
        }
    }

	    private boolean isEmpty() {
			// TODO Auto-generated method stub
			throw new UnsupportedOperationException("Unimplemented method 'isEmpty'");
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