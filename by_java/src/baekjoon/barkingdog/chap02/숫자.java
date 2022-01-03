package baekjoon.barkingdog.chap02;

import java.util.Scanner;

public class 숫자 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        long a = scanner.nextLong();
        long b = scanner.nextLong();

        if(a>b) {
            System.out.println(a-b-1);
            for(long i=b+1; i<a; i++) {
                System.out.print(i + " ");
            }
        }
        if(b>a) {
            System.out.println(b-a-1);
            for(long i=a+1; i<b; i++) {
                System.out.print(i + " ");
            }
        }
        if(a==b) {
            System.out.println(0);
        }
    }
}
