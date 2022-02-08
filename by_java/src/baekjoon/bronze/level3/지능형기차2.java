package baekjoon.bronze.level3;

import java.util.Scanner;

public class 지능형기차2 {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);

        int max = 0;
        int current = 0;

        for(int i=0; i<10; i++) {
            int a = scanner.nextInt();
            int b = scanner.nextInt();

            current = current - a + b;
            max = Math.max(max, current);
        }
        System.out.println(max);
    }
}
