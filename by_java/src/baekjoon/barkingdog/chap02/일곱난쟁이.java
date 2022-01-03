package baekjoon.barkingdog.chap02;

import java.util.Arrays;
import java.util.Scanner;

public class 일곱난쟁이 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = 9;
        int[] a = new int[n];
        int sum = 0;
        for(int i=0; i<n; i++) {
            a[i] = scanner.nextInt();
            sum += a[i];
        }
        Arrays.sort(a);
        for(int i=0; i<n; i++) {
            for (int j = i+1; j<n; j++) {
                if(sum - a[i] - a[j] == 100) {
                    for(int k=0; k<n; k++) {
                        if(i==k || j==k) {
                            continue;
                        }
                        System.out.println(a[k]);
                    }
                }
            }
        }
    }
}
