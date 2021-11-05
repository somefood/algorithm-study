package level06_function;

import java.util.Scanner;

public class Prac15596 {
    static long sum(int[] a) {
        long result = 0;
        for(int i=0; i<a.length; i++) {
            result += a[i];
        }
        return result;
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        int[] arr = new int[n];
        for(int i=0; i<n; i++) {
            arr[i] = scan.nextInt();
        }
        System.out.println(sum(arr));
    }
}
