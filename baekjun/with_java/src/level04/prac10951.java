package level04;

import java.util.Scanner;

public class prac10951 {
    public static void main(String[] args) throws java.io.IOException {
        Scanner scan = new Scanner(System.in);
        int A, B;
        while (scan.hasNextInt()) {
            A = scan.nextInt();
            B = scan.nextInt();
            System.out.println(A + B);
        }
    }
}