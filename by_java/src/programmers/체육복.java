package programmers;

import java.util.Arrays;

public class 체육복 {
    public static int solution(int n, int[] lost, int[] reserve) {
        int answer = 0;
        int size = n + 1;
        int[] student = new int[size];

        for(int i=1; i<size; i++) {
            student[i]++;
        }

        for (int i : reserve) {
            student[i]++;
        }

        for (int i: lost) {
            student[i]--;
        }

        for (int i=1; i<size-1; i++) {
            if(student[i] >= 1) continue;
            if(student[i - 1] >= 2) {
                student[i - 1]--;
                student[i]++;
            } else if(student[i +1] >= 2) {
                student[i +1]--;
                student[i]++;
            }
        }
        System.out.println(Arrays.toString(student));
        for(int i=1; i<size; i++) {
            if (student[i] >= 1) answer++;
        }
        return answer;
    }

    public static void main(String[] args) {
        System.out.println(solution(5, new int[]{2, 4}, new int[]{1, 3, 5}));
        System.out.println(solution(5, new int[]{2, 4}, new int[]{3}));
        System.out.println(solution(3, new int[]{3}, new int[]{1}));
    }
}
