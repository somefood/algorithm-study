package chap02;

import java.util.NoSuchElementException;

class Node <E> {
    private E item;
    private Node<E> next;

    Node(E newItem, Node<E> node) {
        item = newItem;
        next = node;
    }

    public E getItem() {return item;}
    public Node<E> getNext() {return next;}
    public void setItem(E newItem) {item = newItem;}
    public void setNext(Node<E> newNext) {next = newNext;}
}

public class SList <E> {
    protected Node head;
    private int size;
    public SList() {
        head = null;
        size = 0;
    }

    public int search(E target) {
        Node p = head;
        for (int k=0; k<size; k++) {
            if(target == p.getItem()) return k;
            p = p.getNext();
        }
        return -1;
    }

    public void insertFront(E newItem) {
        head = new Node(newItem, head);
        size++;
    }

    public void insertAfter(E newItem, Node p) {
        p.setNext(new Node(newItem, p.getNext()));
        size++;
    }

    public void deleteFront() {
        if(size <= 0) throw new NoSuchElementException();
        head = head.getNext();
        size--;
    }

    public void deleteAfter(Node p) {
        if (p == null) throw new NoSuchElementException();
        Node t = p.getNext();
        p.setNext(t.getNext());
        t.setNext(null);
        size--;
    }
}
