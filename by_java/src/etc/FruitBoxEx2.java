package etc;

import java.util.ArrayList;

class Fruit2 implements Eatable {
    public String toString() {
        return "Fruit";
    }
}

interface Eatable {}

public class FruitBoxEx2 {
    public static void main(String[] args) {

    }
}

class FruitBox2<T extends Fruit & Eatable> extends Box<T> {}

class Box<T> {
    ArrayList<T> list = new ArrayList<>();
    void add(T item) {
        list.add(item);
    }

    T get(int i) {
        return list.get(i);
    }

    public String toString() {
        return list.toString();
    }
}