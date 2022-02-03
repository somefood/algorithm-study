package baekjoon.bronze.level5;

import java.math.BigInteger;
import java.util.Scanner;

public class 엄청난부자2 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String s1 = scanner.next();
        String s2 = scanner.next();

        BigInteger n = new BigInteger(s1);
        BigInteger m = new BigInteger(s2);

        System.out.println(n.divide(m));
        System.out.println(n.remainder(m));
    }
}
