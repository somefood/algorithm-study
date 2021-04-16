package level04;

import java.util.Scanner;

public class prac10952 {
    public static void main(String[] args){
        int A, B;
        Scanner scan = new Scanner(System.in);
        while (true) {
            A = scan.nextInt();
            B = scan.nextInt();
            if(A == 0 && B == 0) break;
            System.out.println(A+B);
        }
    }
}