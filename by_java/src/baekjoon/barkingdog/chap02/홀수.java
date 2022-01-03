package baekjoon.barkingdog.chap02;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

public class 홀수 {
    static void fun(List<Integer> list) {
        int sum = 0;
        if (list.size() <= 0)
            System.out.println(-1);
        else {
            for (int i = 0; i < list.size(); i++) {
                sum += list.get(i);
            }
            System.out.println(sum);
            System.out.println(Collections.min(list));
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        List<Integer> list = new ArrayList<>();
        int val = 0;
        for (int i = 0; i < 7; i++) {
            val = scanner.nextInt();
            if (val % 2 != 0) {
                list.add(val);
            }
        }
        fun(list);
    }
}
