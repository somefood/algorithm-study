package doit.chap03;

import java.util.Scanner;

public class SeqSearch {
    static int seqSearch(int[] a, int n, int key) {
        int i = 0;

        while (true) {
            if (i == n)
                return -1;
            if (a[i] == key)
                return i;
            i++;
        }
    }

    static int seqSearchWithFor(int[] a, int n, int key) {
        int i = 0;

        for(i=0; i<n; i++) {
            if(a[i] == key)
                return i;
        }
        return -1;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[] x = new int[]{22, 8, 55, 32, 120, 55, 70};
        int num = x.length;
        System.out.print("검색할 값:");
        int ky = scanner.nextInt();

        int idx = seqSearch(x, num, ky);
        if(idx == - 1)
            System.out.println("no element");
        else
            System.out.println("The element is in " + idx);
        int idxf = seqSearch(x, num, ky);
        if(idxf == - 1)
            System.out.println("no element");
        else
            System.out.println("The element is in " + idxf);
    }
}
