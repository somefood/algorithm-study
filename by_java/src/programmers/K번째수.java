package programmers;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class K번째수 {
    public static int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        int top = 0;
        List<Integer> list = new ArrayList<>();
        for (int i : array) {
            list.add(i);
        }

        for (int[] command : commands) {
            int i = command[0];
            int j = command[1];
            int k = command[2];
            List<Integer> temp = new ArrayList<>();
            for(int a=i-1; a<j; a++) {
                temp.add(list.get(a));
            }
            Collections.sort(temp);
            answer[top++] = temp.get(k-1);
        }
        return answer;
    }

    public static void main(String[] args) {
        System.out.println(Arrays.toString(solution(new int[]{1, 5, 2, 6, 3, 7, 4}, new int[][]{{2, 5, 3}, {4, 4, 1}, {1, 7, 3}})));
    }
}
