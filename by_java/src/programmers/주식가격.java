package programmers;

import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;

public class 주식가격 {
    public int[] solution(int[] prices) {
        int[] answer = new int[prices.length];
        int top = 0;
        Stack<Integer> stack = new Stack<>();
        for(int i= prices.length-1; i >= 0; i--) {
            stack.push(prices[i]);
        }

        while(!stack.isEmpty()) {
            int current = stack.pop();
            int cnt = 0;
            for(int i=stack.size()-1; i>=0; i--) {
                if(current <= stack.get(i)) cnt++;
                else {
                    cnt += 1;
                    break;
                }
            }
            answer[top++] = cnt;
        }
        return answer;
    }
    public static void main(String[] args) {
        주식가격 t = new 주식가격();
        System.out.println(Arrays.toString(t.solution(new int[]{1, 2, 3, 2, 3})));
        System.out.println(Arrays.toString(t.solution(new int[]{1, 2, 1, 1, 1})));
        System.out.println(Arrays.toString(t.solution(new int[]{1, 2})));
        System.out.println(Arrays.toString(t.solution(new int[]{2, 1, 4})));
    }
}
