package programmers;

import java.util.Iterator;
import java.util.LinkedList;
import java.util.Queue;

public class 다리를지나는트럭 {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        Queue<Integer> queue = new LinkedList<>();
        int answer = 0;
        int sum = 0;

        for (int truck : truck_weights) {
            while (true) {
                if(queue.isEmpty()) {
                    queue.add(truck);
                    sum += truck;
                    answer++;
                    break;
                } else if(queue.size() == bridge_length) {
                    sum -= queue.poll();;
                } else {
                    if (sum + truck <= weight) {
                        queue.add(truck);
                        sum += truck;
                        answer++;
                        break;
                    } else {
                        queue.add(0);
                        answer++;
                    }
                }
            }
        }

        return answer + bridge_length;
    }

    public static void main(String[] args) {
        다리를지나는트럭 t = new 다리를지나는트럭();
        System.out.println(t.solution(2, 10, new int[]{7, 4, 5, 6}));
        System.out.println(t.solution(100, 100, new int[]{10}));
        System.out.println(t.solution(100, 100, new int[]{10, 10, 10, 10, 10, 10, 10, 10, 10, 10}));
    }
}
