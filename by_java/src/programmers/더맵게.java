package programmers;

import java.util.PriorityQueue;

public class 더맵게 {
    public static int solution(int[] scoville, int K) {
        int answer = 0;
        PriorityQueue<Integer> heap = new PriorityQueue<>();
        for (int i : scoville) {
            heap.add(i);
        }
        int count = 0;
        while(!heap.isEmpty() && heap.size() > 1) {
            int a = heap.poll();
            int b = heap.poll();
            heap.add(a + b * 2);
            count++;
            if(heap.element() >= K) return count;
        }

        return -1;
    }

    public static void main(String[] args) {
        System.out.println(solution(new int[]{1, 2, 3, 9, 10, 12}, 7));
    }
}
