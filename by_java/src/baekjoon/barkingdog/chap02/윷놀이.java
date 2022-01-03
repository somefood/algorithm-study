package baekjoon.barkingdog.chap02;

import java.util.Scanner;

public class 윷놀이 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        for(int i=0; i<3; i++) {
            int count = 0;
            for(int j=0; j<4; j++) {
                if(scanner.nextInt() == 0)
                    count++;
                else
                    continue;
            }
            if (count == 1)
                System.out.println("A");
            else if(count == 2)
                System.out.println("B");
            else if(count == 3)
                System.out.println("C");
            else if(count == 4)
                System.out.println("D");
            else
                System.out.println("E");
        }
    }
}
