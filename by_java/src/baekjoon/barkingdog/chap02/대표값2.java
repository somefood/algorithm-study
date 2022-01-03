package baekjoon.barkingdog.chap02;

import java.util.Arrays;
import java.util.Scanner;

public class 대표값2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[] arr = new int[5];

        int sum = 0;
        for(int i=0; i<arr.length; i++) {
            int n = scanner.nextInt();
            arr[i] = n;
            sum += n;
        }
        Arrays.sort(arr);
        System.out.println(sum/5);
        System.out.println(arr[5/2]);
    }
}
