public class Prac03 {
    static void func(int a, int b, int n) {
        if(n == 1) {
            System.out.println(a + " " + b);
            return;
        }
        func(a, 6-a-b, n-1);
        System.out.println(a + " " + b);
        func(6-a-b, b, n-1);
    }
    public static void main(String[] args) {
        int k = 3;
        func(1, 3, k);
    }
}