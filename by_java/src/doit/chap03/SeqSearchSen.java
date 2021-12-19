package doit.chap03;

import java.util.Scanner;

public class SeqSearchSen {
    static int seqSearchSen(int[] a, int n, int key) {
        int i=0;

        a[n] = key;

        while(true) {
            if(a[i] == key)
                break;
            i++;
        }
        return i == n ? -1 : i;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[] x = new int[]{22, 8, 55, 32, 120, 55, 70, 0};
        int num = x.length - 1;
        System.out.print("검색할 값:");
        int ky = scanner.nextInt();

        int idx = seqSearchSen(x, num, ky);
        if(idx == - 1)
            System.out.println("no element");
        else
            System.out.println("The element is in " + idx);
    }
}
