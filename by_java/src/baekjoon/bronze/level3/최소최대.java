package baekjoon.bronze.level3;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

public class 최소최대 {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);

        int n = scanner.nextInt();
        List<Integer> arr = new ArrayList<>();
        for(int i=0; i<n; i++) {
            arr.add(scanner.nextInt());
        }

        System.out.print(Collections.min(arr) + " " + Collections.max(arr));
    }
}
