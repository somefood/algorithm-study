package baekjoon.barkingdog.chap02;

import java.util.Scanner;

public class 별찍기8 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();

        for(int i=0; i<n; i++) {
            for(int j=0; j<i+1; j++) {
                System.out.print("*");
            }
            for(int k=2*(n-i)-2; k>0; k--) {
                System.out.print(" ");
            }
            for(int l=0; l<i+1; l++) {
                System.out.print("*");
            }
            System.out.println();
        }
        for(int i=n-1; i>0; i--) {
            for(int j=i; j>0; j--) {
                System.out.print("*");
            }
            for(int k=0; k<2*(n-i);k++) {
                System.out.print(" ");
            }
            for(int j=i; j>0; j--) {
                System.out.print("*");
            }
            System.out.println();
        }
    }
}
