package programmers;

import java.util.Arrays;

public class 카펫 {

    public static int[] solution(int brown, int yellow) {
        int sum = brown + yellow;
        int[] answer = new int[2];
        for(int i=1; i<=sum; i++) {
            for(int j=1; j<=sum; j++) {
                if(j > i) continue;
                if(i * j == sum) {
                    if((i-2) * (j-2) == yellow)
                    {
                        answer[0] = i;
                        answer[1] = j;
                        return answer;
                    }
                }
            }
        }
        return answer;
    }

    public static void main(String[] args) {
        System.out.println(Arrays.toString(solution(10, 2)));
        System.out.println(Arrays.toString(solution(8, 1)));
        System.out.println(Arrays.toString(solution(24, 24)));
    }
}
