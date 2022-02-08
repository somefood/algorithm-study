package baekjoon.bronze.level5;

import java.util.Scanner;

public class 킹퀸룩비숍 {
    static int[] chess = {1, 1, 2, 2, 2, 8};
    static int[] result = new int[6];

    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        for(int i=0; i<6; i++) {
            int num = scanner.nextInt();
            if (chess[i] != num) result[i] = chess[i] - num;
            else result[i] = 0;
        }

        for(int i=0; i<6; i++) {
            System.out.print(result[i] + " ");
        }
    }
}
