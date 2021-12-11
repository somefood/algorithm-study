package doit.chap02;

public class IntArray {
    public static void main(String[] args) {
        int[] a = new int[5];

        a[1] = 37;
        a[2] = 51;
        a[4] = a[1] * 2;

        for (int i : a) {
            System.out.println(i);
        }
    }
}
