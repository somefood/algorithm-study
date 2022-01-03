package baekjoon.barkingdog.chap02;

import java.util.Scanner;

public class 핸드폰요금 {

    static int[] result = new int[2];

    static void calc(int n) {
        result[0] += (n/30 + 1) * 10;
        result[1] += (n/60 + 1) * 15;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        for(int i=0; i<n; i++) {
            calc(scanner.nextInt());
        }
        if(result[0] > result[1]) {
            System.out.print("M " + result[1]);
        } else if(result[0] < result[1]) {
            System.out.print("Y " + result[0]);
        } else {
            System.out.print("Y M " + result[0]);
        }
    }
}
