package etc;


import java.util.ArrayList;
import java.util.List;

class Fruit {
    String name;
    int count;

    public Fruit() {
        System.out.println("기본 생성자 호출");
    }

    public Fruit(String name, int count) {
        this.name = name;
        this.count = count;
    }

    @Override
    public String toString() {
        return "Fruit{" +
                "name='" + name + '\'' +
                ", count=" + count +
                '}';
    }
}

class Apple extends Fruit {

    public Apple(String name, int count) {
        this.name = name;
        this.count = count;
    }
}

class Toy {
    String name;
    int count;
}

class FruitBox<T extends Fruit> {

    List<T> box = new ArrayList<>();

    void showBox() {
        for (T fruit : box) {
            System.out.println(fruit);
        }
    }
}

public class GenericTest {

    public static void main(String[] args) {
        FruitBox<Fruit> fruitBox = new FruitBox<>();
        fruitBox.box.add(new Fruit("사과", 2));
        fruitBox.box.add(new Fruit("배", 2));

        fruitBox.showBox();

        FruitBox<Apple> box = new FruitBox<>();
    }
}
