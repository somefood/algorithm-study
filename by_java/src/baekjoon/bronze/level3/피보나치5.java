package baekjoon.bronze.level3;

import java.util.Scanner;

public class 피보나치5 {

    static int fibo(int n) {
        if(n == 0) return 0;
        if(n == 1) return 1;
        return fibo(n-1) + fibo(n-2);
    }

    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();

        System.out.println(fibo(n));
    }
}
