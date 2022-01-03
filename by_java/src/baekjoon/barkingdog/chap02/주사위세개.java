package baekjoon.barkingdog.chap02;

import java.util.Scanner;

public class 주사위세개 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int a = scanner.nextInt();
        int b = scanner.nextInt();
        int c = scanner.nextInt();

        int money = 0;

        if (a == b && b == c)
            money = 10000 + a * 1000;
        else if (a == b) {
            money = 1000 + a * 100;
        } else if (a == c) {
            money = 1000 + a * 100;
        } else if (b == c) {
            money = 1000 + b * 100;
        } else if (a != b && b != c) {
            int t = Math.max(a, b);
            t = Math.max(t, c);
            money = t * 100;
        }
        System.out.println(money);
    }
}
