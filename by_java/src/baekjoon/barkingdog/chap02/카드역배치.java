package baekjoon.barkingdog.chap02;

import java.util.Arrays;
import java.util.Scanner;

public class 카드역배치 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[] arr = new int[21];
        for(int i=1; i<21; i++) {
            arr[i] = i;
        }

        int a, b;
        int min, max;
        int temp = 0;
        for(int i=0; i<10; i++) {
            a = scanner.nextInt();
            b = scanner.nextInt();
            min = Math.min(a, b);
            max = Math.max(a, b);
            for(int j=min, k=0; j<=(max+min)/2; j++, k++) {
                temp = arr[j];
                arr[j] = arr[max-k];
                arr[max-k] = temp;
            }
            System.out.println(Arrays.toString(arr));
        }
        for(int i=1; i<21; i++) {
            System.out.print(arr[i] + " ");
        }
    }
}
