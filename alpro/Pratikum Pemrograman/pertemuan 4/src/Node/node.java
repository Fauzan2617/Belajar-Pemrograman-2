package Node;

public class node {
    double data;
    node next;
    
    public node(double data) {
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
}