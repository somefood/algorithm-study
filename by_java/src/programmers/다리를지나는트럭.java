package programmers;

import java.util.LinkedList;
import java.util.Queue;

public class 다리를지나는트럭 {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int answer = 0;
        Queue<Integer> completed = new LinkedList<>();
        Queue<Integer> ing = new LinkedList<>();
        Queue<Integer> start = new LinkedList<>();
        for (int truck_weight : truck_weights) {
            start.add(truck_weight);
        }

        while(!start.isEmpty()) {
            int truck = start.peek();
            int bridgeTotal = 0;
            for (Integer integer : ing) {
                bridgeTotal += integer;
            }
            if((bridgeTotal + truck) < weight) {
                ing.add(truck);
                start.poll();
            }
            answer++;
            if((answer % bridge_length) == 0) {
                ing.poll();
            }
        }
        return answer;
    }

    public static void main(String[] args) {
        다리를지나는트럭 t = new 다리를지나는트럭();
        System.out.println(t.solution(2, 10, new int[]{7, 4, 5, 6}));
        System.out.println(t.solution(100, 100, new int[]{10}));
        System.out.println(t.solution(100, 100, new int[]{10, 10, 10, 10, 10, 10, 10, 10, 10, 10}));
    }
}
