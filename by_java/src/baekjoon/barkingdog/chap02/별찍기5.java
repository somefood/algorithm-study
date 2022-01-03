package baekjoon.barkingdog.chap02;

import java.util.Scanner;

public class 별찍기5 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();

        for(int i=1; i<=n; i++) {
            for(int j=n-i; j>0; j--) {
                System.out.print(" ");
            }
            for(int k=1; k<=2*i-1; k++) {
                System.out.print("*");
            }
            System.out.println();
        }
    }
}
