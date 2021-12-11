package programmers;

import java.util.HashMap;

public class 위장 {

    public int solution(String[][] clothes) {
        int answer = 1;
        HashMap<String, Integer> hashMap = new HashMap<>();
        for (int i = 0; i < clothes.length; i++) {
            String name = clothes[i][0];
            String sort = clothes[i][1];

            hashMap.put(sort, hashMap.getOrDefault(sort, 0) + 1);
        }

        for (Integer value : hashMap.values()) {
            answer *= (value + 1);
        }
        return answer - 1;
    }

    public static void main(String[] args) {
        위장 t = new 위장();

        // 5
        System.out.println(t.solution(new String[][]{
                {"yellowhat", "headgear"},
                {"bluesunglasses", "eyewear"},
                {"green_turban", "headgear"}}));
    }
}
