package level07_str;

import java.util.Scanner;

public class Prac11720 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        String str = scan.next();
        int result = 0;
        for(int i=0; i<n; i++) {
            result += str.charAt(i) - '0';
        }
        System.out.println(result);
    }
}
