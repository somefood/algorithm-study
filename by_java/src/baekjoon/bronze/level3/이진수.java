package baekjoon.bronze.level3;

import java.util.Scanner;

public class 이진수 {
    static void get1OfBinary(int n) {
        StringBuilder sb = new StringBuilder();
        while (n != 1) {
            sb.append(n % 2);
            n = n / 2;
        }
        sb.append(1);
        String s = sb.toString();
        char[] chars = s.toCharArray();
        for(int i=0; i<chars.length; i++) {
            if(chars[i] == '1') System.out.print(i + " ");
        }
        System.out.println();
    }

    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt();
        for(int i=0; i<t; i++) {
            get1OfBinary(scanner.nextInt());
        }
    }
}
