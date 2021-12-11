package level1;

import java.util.ArrayList;
import java.util.Arrays;

public class 기능개발 {
    public int[] solution(int[] progresses, int[] speeds) {
        int[] temp = new int[100];
        int[] answer = new int[100];
        int top = 0;
        int aTop = 0;
        for(int i=0; i<progresses.length; i++) {
            double progress = progresses[i];
            double speed = speeds[i];
            temp[top++] = (int) Math.ceil((100-progress)/speed);
        }

        ArrayList<Integer> list = new ArrayList<>();
        for (int i = 0; i < top; i++) {
            int origin = temp[i];
            int count = 1;
            if (origin < 0) {
                continue;
            }
            for (int j = i + 1; j < top; j++) {
                int compare = temp[j];
                if (origin >= compare) {
                    temp[j] = -1;
                    count++;
                } else {
                    break;
                }
            }
            list.add(count);
        }

        answer = list.stream().mapToInt(i ->i).toArray();
        return answer;
    }

    public static void main(String[] args) {
        기능개발 t = new 기능개발();
        System.out.println(t.solution(new int[]{93, 30, 55}, new int[]{1, 30, 5}));
        System.out.println(t.solution(new int[]{95, 90, 99, 99, 80, 99}, new int[]{1, 1, 1, 1, 1, 1}));
    }
}
