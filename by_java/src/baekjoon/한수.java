package baekjoon;

import java.util.Scanner;

public class 한수 {
    public static int hansu(int n) {
        if (n < 100) return n;
        int count = 0;
        for (int i = 100; i <= n; i++) {
            int a = i / 100;
            int b = i % 100 / 10;
            int c = i % 100 % 10;
            if((b-a) == (c-b)) count++;
        }
        return 99 + count;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        System.out.println(hansu(n));
    }
}
