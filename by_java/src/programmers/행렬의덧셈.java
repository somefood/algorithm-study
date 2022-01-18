package programmers;

import java.util.Arrays;

public class 행렬의덧셈 {
    public static int[][] solution(int[][] arr1, int[][] arr2) {
        int size = arr1.length;
        int[][] answer = new int[size][arr1[0].length];
        for(int i=0; i<size; i++) {
            for(int j=0; j<arr1[i].length; j++) {
                answer[i][j] = arr1[i][j] + arr2[i][j];
            }
        }
        return answer;
    }

    public static void main(String[] args) {
        System.out.println(Arrays.deepToString(solution(new int[][]{{1, 2}, {2, 3}}, new int[][]{{3, 4}, {5, 6}})));
        System.out.println(Arrays.deepToString(solution(new int[][]{{1}, {2}}, new int[][]{{3}, {4}})));
    }
}
