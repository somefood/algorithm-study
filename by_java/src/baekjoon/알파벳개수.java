package baekjoon;

import java.util.Arrays;
import java.util.Scanner;

public class 알파벳개수 {

    static int[] solution(String s) {
        int[] arr = new int[26];

        for(int i=0; i<s.length(); i++) {
            char c = s.charAt(i);
            arr[c-'a']++;
        }
        return arr;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String s = scanner.next();
        int[] result = solution(s);
        for (int i : result) {
            System.out.print(i + " ");
        }
    }
}
