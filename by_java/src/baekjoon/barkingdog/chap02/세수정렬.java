package baekjoon.barkingdog.chap02;

import java.util.Scanner;

public class 세수정렬 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[] array = new int[3];

        array[0] = scanner.nextInt();
        array[1] = scanner.nextInt();
        array[2] = scanner.nextInt();

        int temp;

        for (int i=0; i < array.length; i++) {
            for (int j=i+1; j< array.length; j++) {
                if(array[i] > array[j]) {
                    temp = array[i];
                    array[i] = array[j];
                    array[j] = temp;
                }
            }
        }

        for (int i : array) {
            System.out.print(i + " ");
        }
    }
}
