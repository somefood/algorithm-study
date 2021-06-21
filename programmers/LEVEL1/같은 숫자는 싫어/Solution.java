public class Solution {
    public int[] solution(int []arr) {
        int[] answer = new int[arr.length];
        int main = arr[0];
        int size = 0;
        answer[size++] = main;

        for(int i=1; i<arr.length; i++) {
            if(main != arr[i]) {
                answer[size++] = arr[i];
                main = arr[i];
            }
        }
        int[] answer2 = new int[size];
        for(int i=0; i<size; i++) {
            answer2[i] = answer[i];
        }
        return answer2;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        int[] arr = {1, 1, 3, 3, 0, 1, 1};
        int[] a = s.solution(arr);
        for(int i: a) {
            System.out.print(i);
        }
    }
}