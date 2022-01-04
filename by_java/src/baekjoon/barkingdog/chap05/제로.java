package baekjoon.barkingdog.chap05;

import java.util.Scanner;
import java.util.Stack;

public class 제로 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Stack<Integer> stack = new Stack<>();
        int n = scanner.nextInt();

        for(int i=0; i<n; i++) {
            int value = scanner.nextInt();
            if(value == 0) stack.pop();
            else stack.add(value);
        }

        int sum = 0;
        while(!stack.isEmpty()) {
            sum += stack.pop();
        }

        System.out.println(sum);
    }
}
