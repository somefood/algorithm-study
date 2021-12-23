package baekjoon;

import java.util.Scanner;

public class 구구단 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        for(int i=1; i<10; i++) {
            System.out.printf("%d * %d = %d", n, i, n*i);
            System.out.println();
        }
    }
}
