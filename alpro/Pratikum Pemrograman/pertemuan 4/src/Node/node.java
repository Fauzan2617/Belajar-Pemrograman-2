package Node;

public class node {
    double data;
    node next;
    
    node(double data) {
        this.data = data;
        this.next = null;
    }
    public double getData() {
        return data;
    }

    public node getNext() {
        return next;
    }

    public void setNext(node next) {
        this.next = next;
    }
    
    // tambahkan method ini jika getNilai() seharusnya merujuk ke data
    public double getNilai() {
        return data;
	}
}