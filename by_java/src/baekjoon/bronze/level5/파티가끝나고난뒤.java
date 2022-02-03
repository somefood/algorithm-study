package baekjoon.bronze.level5;

import java.io.BufferedWriter;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.util.Scanner;

public class 파티가끝나고난뒤 {
    public static void main(String[] args) throws IOException {
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        Scanner scanner = new Scanner(System.in);
        int L = scanner.nextInt();
        int P = scanner.nextInt();

        int sum = L * P;

        for(int i=0; i<5; i++) {
            bw.write(scanner.nextInt() - sum + " ");
        }
        bw.flush();
        bw.close();
    }
}
