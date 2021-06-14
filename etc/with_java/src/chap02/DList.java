package chap02;

import java.util.NoSuchElementException;

class DNode <E> {
    private E item;
    private DNode previous;
    private DNode next;
    public DNode(E newItem, DNode p, DNode q) {
        item = newItem;
        previous = p;
        next = q;
    }
    public  E getItem() {return item;}
    public DNode getPrevious() {return previous;}
    public DNode getNext() {return next;}
    public void setItem(E newItem) {item = newItem;}
    public void setPrevious(DNode p) {previous = p;}
    public void setNext(DNode q) {next = q;}
}

public class DList <E> {
    protected DNode head, tail;
    protected int size;
    public DList() {
        head = new DNode(null, null, null);
        tail = new DNode(null, head, null);
        head.setNext(tail);
        size = 0;
    }

    public void insertBefore(DNode p, E newItem) {
        DNode t = p.getPrevious();
        DNode newNode = new DNode(newItem, t, p);
        p.setPrevious(newNode);
        t.setNext(newNode);
        size++;
    }

    public void insertAfter(DNode p, E newItem) {
        DNode t = p.getNext();
        DNode newNode = new DNode(newItem, p, t);
        t.setPrevious(newNode);
        p.setNext(newNode);
        size++;
    }

    public void delete(DNode x) {
        if ( x== null) throw new NoSuchElementException();
        DNode f = x.getPrevious();
        DNode r = x.getNext()
        f.setNext(r);
        r.setPrevious(f);
        size--;
    }
}
