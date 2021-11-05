class Seokju {
    public long[] solution(long x, int n) {
        long[] answer = new long[n];
        long step = x;
        for(int i=0; i<n; i++) {
            answer[i] = step;
            step += x;
        }
        return answer;
    }
}