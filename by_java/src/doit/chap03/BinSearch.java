package doit.chap03;

import java.util.Scanner;

public class BinSearch {
    static int binSearch(int[] a, int n, int key) {
        int pl = 0;
        int pr = n - 1;

        do {
            int pc = (pl + pr) / 2;
            if (a[pc] == key)
                return pc;
            else if (a[pc] < key)
                pl = pc + 1;
            else
                pr = pc - 1;
        } while (pl <= pr);
        return -1;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int[] x = {1, 4, 10, 20, 50, 100 ,190 ,350};
        int num = x.length;
        System.out.print("검색: ");
        int ky = scanner.nextInt();

        int idx = binSearch(x, num, ky);
        if(idx == - 1)
            System.out.println("no element");
        else
            System.out.println("The element is in " + idx);
    }
}
