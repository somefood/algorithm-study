package datastructure;

import java.util.Arrays;
import java.util.Comparator;
import java.util.NoSuchElementException;
import java.util.Random;

public class Heap<E> {

    private final Comparator<? super E> comparator;
    private static final int DEFAULT_CAPACITY = 10;

    private int size;

    private Object[] array;

    public Heap() {
        this(null);
    }

    public Heap(Comparator<? super E> comparator) {
        this.array = new Object[DEFAULT_CAPACITY];
        this.size = 0;
        this.comparator = comparator;
    }

    public Heap(int capacity) {
        this(capacity, null);
    }

    public Heap(int capacity, Comparator<? super E> comparator) {
        this.array = new Object[capacity];
        this.size = 0;
        this.comparator = comparator;
    }

    private int getParent(int index) {
        return index / 2;
    }

    private int getLeftChild(int index) {
        return index * 2;
    }

    private int getRightChild(int index) {
        return index * 2 + 1;
    }

    private void resize(int newCapacity) {
        Object[] newArray = new Object[newCapacity];

        for (int i = 1; i <= size; i++) {
            newArray[i] = array[i];
        }

        this.array = null;
        this.array = newArray;
    }

    public void add(E value) {
        if (size + 1 == array.length) {
            resize(array.length * 2);
        }

        shiftUp(size + 1, value);
        size++;
    }

    private void shiftUp(int idx, E target) {
        if (comparator != null) {
            shiftUpComparator(idx, target, comparator);
        } else {
            shiftUpComparable(idx, target);
        }
    }

    private void shiftUpComparator(int idx, E target, Comparator<? super E> comp) {
        while (idx > 1) {
            int parent = getParent(idx);
            Object parentVal = array[parent];

            if (comp.compare(target, (E) parentVal) >= 0) {
                break;
            }
            array[idx] = parentVal;
            idx = parent;
        }
        array[idx] = target;
    }

    @SuppressWarnings("unchecked")
    private void shiftUpComparable(int idx, E target) {
        Comparable<? super E> comp = (Comparable<? super E>) target;

        while (idx > 1) {
            int parent = getParent(idx);
            Object parentVal = array[parent];

            if (comp.compareTo((E) parentVal) >= 0) {
                break;
            }
            array[idx] = parentVal;
            idx = parent;
        }
        array[idx] = comp;
    }

    @SuppressWarnings("unchecked")
    public E remove() {
        if (array[1] == null) {
            throw new NoSuchElementException();
        }

        E result = (E) array[1];
        E target = (E) array[size];
        array[size] = null;

        shiftDown(1, target);

        return result;
    }

    private void shiftDown(int idx, E target) {
        if (comparator != null) {
            shiftDownComparator(idx, target, comparator);
        } else {
            shiftDownComparable(idx, target);
        }
    }

    private void shiftDownComparator(int idx, E target, Comparator<? super E> comp) {
        array[idx] = null;
        size--;

        int parent = idx;
        int child;

        while ((child = getLeftChild(parent)) <= size) {
            int right = getRightChild(parent);

            Object childVal = array[child];

            if (right <= size && comp.compare((E) childVal, (E) array[right]) > 0) {
                child = right;
                childVal = array[child];
            }

            if (comp.compare(target, (E) childVal) <= 0) {
                break;
            }
            array[parent] = childVal;
            parent = child;
        }
        array[parent] = target;

        if (array.length > DEFAULT_CAPACITY && size < array.length / 4) {
            resize(Math.max(DEFAULT_CAPACITY, array.length) / 2);
        }
    }

    private void shiftDownComparable(int idx, E target) {

        Comparable<? super E> comp = (Comparable<? super E>) target;

        array[idx] = null;
        size--;

        int parent = idx;
        int child;

        while ((child = getLeftChild(parent)) <= size) {

            int right = getRightChild(parent);

            Object childVal = array[child];

            if (right <= size && ((Comparable<? super E>) childVal).compareTo((E) array[right]) > 0) {
                child = right;
                childVal = array[child];
            }

            if (comp.compareTo((E) childVal) <= 0) {
                break;
            }
            array[parent] = childVal;
            parent = child;

        }
        array[parent] = comp;

        if (array.length > DEFAULT_CAPACITY && size < array.length / 4) {
            resize(Math.max(DEFAULT_CAPACITY, array.length / 2));
        }
    }

    public int size() {
        return this.size;
    }

    @SuppressWarnings("unchecked")
    public E peek() {
        if (array[1] == null) {
            throw new NoSuchElementException();
        }

        return (E) array[1];
    }

    public boolean isEmpty() {
        return size == 0;
    }

    public Object[] toArray() {
        return Arrays.copyOf(array, size + 1);
    }
}


class test {
    public static void main(String[] args) {
        Heap<Integer> heap = new Heap<>();

        Random random = new Random();

        for(int i=0; i<15; i++) {
            heap.add(random.nextInt(100));
        }

        System.out.println("내부 배열 상태 : ");
        for (Object val : heap.toArray()) {
            System.out.print(val + " ");
        }
        System.out.println();

        System.out.print("힙 요소 뽑기 : \t");
        while (!heap.isEmpty()) {
            System.out.print(heap.remove() + " ");
        }
    }
}
