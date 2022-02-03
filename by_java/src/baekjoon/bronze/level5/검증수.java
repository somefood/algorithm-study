package baekjoon.bronze.level5;

import java.util.Scanner;

public class 검증수 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int sum = 0;
        for (int i = 0; i < 5; i++) {
            sum += Math.pow(scanner.nextInt(), 2);
        }
        System.out.println(sum % 10);
    }
}
