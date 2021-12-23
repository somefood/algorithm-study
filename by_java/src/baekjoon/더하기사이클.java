package baekjoon;

import java.util.Scanner;

public class 더하기사이클 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String n = scanner.next();

        int count = 0;
        String s = n;
        do {
            if (Integer.parseInt(n) < 10) {
                n = "0" + n;
            }
            int a = n.charAt(0) - '0';
            int b = n.charAt(1) - '0';
            int c = (a + b) % 10;
            n = String.valueOf(b * 10 + c);
            count++;
        } while (!s.equals(n));
        System.out.println(count);
    }
}
