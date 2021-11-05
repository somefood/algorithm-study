package chap01;

import java.util.Scanner;

public class Digits {
    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);
        int no;

        System.out.println("2자리의 정수 입력");

        do {
            System.out.print("입력: ");
            no = stdIn.nextInt();
        } while (no < 10 || no > 99);
        System.out.println(no);
    }
}
