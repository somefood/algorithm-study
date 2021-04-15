package level03;

import java.util.Scanner;

public class prac10871 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int N = scan.nextInt();
        int X = scan.nextInt();
        int v;
        for(int i=0; i<N; i++) {
            v = scan.nextInt();
            if (v < X) System.out.print(v+ " ");
        }
    }
}
