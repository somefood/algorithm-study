package baekjoon.barkingdog.chap02;

import java.util.Scanner;

public class 별찍기6 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();

        for(int i=n; i>0; i--) {
            for (int k=0; k<n-i; k++) {
                System.out.print(" ");
            }
            for(int j=2*i-1; j>0; j--) {
                System.out.print("*");
            }
            System.out.println();
        }
    }
}
