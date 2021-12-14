package programmers;

import java.util.Collections;
import java.util.PriorityQueue;

public class 프린터 {
    public int solution(int[] priorities, int location) {
        int answer = 0;
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        for (int priority : priorities) {
            pq.offer(priority);
        }

        while(!pq.isEmpty()) {
            for(int i=0; i<priorities.length; i++) {
                if(priorities[i] == pq.peek()) {
                    pq.poll();
                    answer++;
                    if (location == i) return answer;
                }
            }
        }
        return answer;
    }

    public static void main(String[] args) {
        프린터 t = new 프린터();
        System.out.println(t.solution(new int[]{2, 1, 3, 2}, 2));
        System.out.println(t.solution(new int[]{1, 1, 9, 1, 1, 1}, 0));
    }
}
