package programmers;

import java.util.*;

public class 모의고사 {
    static int[] pattern1 = new int[]{1, 2, 3, 4, 5};
    static int[] pattern2 = new int[]{2, 1, 2, 3, 2, 4, 2, 5};
    static int[] pattern3 = new int[]{3, 3, 1, 1, 2, 2, 4, 4, 5, 5};

    public int[] solution(int[] answers) {
        List<Integer> list = new ArrayList<>(Arrays.asList(0, 0, 0));
        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < answers.length; i++) {
            int currentA = answers[i];
            if (currentA == pattern1[i % pattern1.length]) list.set(0, list.get(0) + 1);
            if (currentA == pattern2[i % pattern2.length]) list.set(1, list.get(1) + 1);
            if (currentA == pattern3[i % pattern3.length]) list.set(2, list.get(2) + 1);
        }

        Integer max = Collections.max(list);
        for (int i = 0; i < list.size(); i++) {
            if (Objects.equals(list.get(i), max))
                result.add(i + 1);
        }
        result.sort(Comparator.naturalOrder());
        int[] answer = new int[result.size()];
        for (int i = 0; i < result.size(); i++) {
            answer[i] = result.get(i);
        }
        return answer;
    }

    public static void main(String[] args) {
        모의고사 t = new 모의고사();
        System.out.println(Arrays.toString(t.solution(new int[]{1, 2, 3, 4, 5})));
        System.out.println(Arrays.toString(t.solution(new int[]{1, 3, 2, 4, 2})));
        System.out.println(Arrays.toString(t.solution(new int[]{1, 1, 1, 1, 1, 1, 1})));
        System.out.println(Arrays.toString(t.solution(new int[]{1, 2, 3, 4, 5, 2, 1, 2, 2, 2, 3, 2, 4, 2, 5})));
    }
}
