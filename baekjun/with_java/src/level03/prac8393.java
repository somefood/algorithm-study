package level03;

import java.util.Scanner;

public class prac8393 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        int sum = 0;
        for(int i=1; i<=n; i++) {
            sum += i;
        }
        System.out.println(sum);
    }
}
