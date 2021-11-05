package chap01;

import java.util.Scanner;

public class JudgeSign {
    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);

        System.out.print("input integer: ");
        int n = stdIn.nextInt();

        if (n >0)
            System.out.println("this value is +");
        else if (n < 0)
            System.out.println("this value is -");
        else
            System.out.println("this value is 0");
    }
}
