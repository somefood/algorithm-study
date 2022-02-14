package programmers;

public class 나라의숫자124 {

    static String[] list = {"4", "1", "2"};

    static public String solution(int n) {
        String answer = "";

        int num = n;
        while(num > 0) {
            int r = num % 3;
            num /= 3;

            if (r == 0) num--;

            answer = list[r] + answer;
        }

        return answer;
    }

    public static void main(String[] args) {
        System.out.println(solution(1));
        System.out.println(solution(2));
        System.out.println(solution(3));
        System.out.println(solution(4));
        System.out.println(solution(5));
        System.out.println(solution(6));
    }
}
