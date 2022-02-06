package baekjoon;

import java.util.Scanner;

public class 팩토리얼 {

    static int fac(int n) {
        if (n == 0) return 1;
        return n * fac(n - 1);
    }

    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();

        System.out.println(fac(n));
    }
}
