package programmers;

import java.util.Arrays;

public class 조이스틱 {
    public static int calc(char c) {
        int upCount = 0;
        int downCount = 0;
        for (int up = 65; up < 91; up++) {
            if (up == c) break;
            upCount++;
        }
        for (int down = 91; down > 64; down--) {
            if (down == c) break;
            downCount++;
        }
        return Math.min(upCount, downCount);
    }

    public static int solution(String name) {
        int answer = 0;
        int size = name.length();
        int[] right = new int[size];
        int[] left = new int[size];
        if(size == 1) return calc(name.charAt(0));

        for(int j=0; j<size; j++) {
            int value = calc(name.charAt(j));
            System.out.println("value = " + value);
            if(j+1 < size) value++;
            right[j] = value;
        }

        for(int k=0; k<size; k++) {
            left[k] = calc(name.charAt(k-size));
        }
        System.out.println(Arrays.toString(right));
        System.out.println(Arrays.toString(left));
        return answer;
    }

    public static void main(String[] args) {
//        System.out.println(solution("JEROEN"));
        System.out.println(solution("AAA"));
        System.out.println(solution("JAZ"));
    }
}
