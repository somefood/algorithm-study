package baekjoon.barkingdog.chap05;

public class StackTest {
    final static int MX = 1000005;
    static int[] data = new int[MX];
    static int pos = 0;

    static void push(int x){
        data[pos++] = x;
    }

    static void pop() {
        --pos;
    }

    static void top() {
        System.out.println(data[pos-1]);
    }

    static void test(){
        push(5); push(4); push(3);
        top(); // 3
        pop(); pop();
        top(); // 5
        push(10); push(12);
        top(); // 12
        pop();
        top(); // 10
    }

    public static void main(String[] args) {
        test();
    }
}
