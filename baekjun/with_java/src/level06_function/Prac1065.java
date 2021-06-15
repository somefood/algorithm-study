package level06_function;

import java.util.Scanner;

public class Prac1065 {
    static int hansu(int n) {
        int count = n <= 99? n : 99;
        for(int i=100; i<=n; i++) {
            String str = String.valueOf(i);
            int num1 = str.charAt(0) - '0';
            int num2 = str.charAt(1) - '0';
            int num3 = str.charAt(2) - '0';
            if(num1 - num2 == num2 - num3) count++;
        }
        return count;
    }
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        System.out.println(hansu(n));
    }
}
