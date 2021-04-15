package level03;

import java.util.Scanner;

public class prac11022 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int A, B;
        int T = scan.nextInt();
        for(int i=1; i<=T; i++){
            A = scan.nextInt();
            B = scan.nextInt();
            System.out.println("Case #" + i +": " + A + " + " + B + " = " + (A+B));
        }
    }
}
