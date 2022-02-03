package baekjoon.bronze.level5;

import java.util.Scanner;

public class 진수16 {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        String hexArray = "0123456789ABCDEF";
        String s = scanner.next();
        int sum = 0;
        for(int i=0; i<s.length(); i++) {
            char c = s.charAt(i);
            int index = hexArray.indexOf(c);
            sum += Math.pow(16, s.length() - i - 1) * index;
        }
        System.out.println(sum);
    }
}
