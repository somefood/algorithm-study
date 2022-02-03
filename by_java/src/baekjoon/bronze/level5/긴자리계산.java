package baekjoon.bronze.level5;

import java.math.BigInteger;
import java.util.Scanner;

public class 긴자리계산 {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        String s1 = scanner.next();
        String s2 = scanner.next();

        BigInteger A = new BigInteger(s1);
        BigInteger B = new BigInteger(s2);

        System.out.println(A.add(B));
        System.out.println(A.subtract(B));
        System.out.println(A.multiply(B));
    }
}
