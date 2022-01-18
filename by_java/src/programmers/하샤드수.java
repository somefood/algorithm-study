package programmers;

public class 하샤드수 {
    public static boolean solution(int x) {
        String s = String.valueOf(x);
        int sum = 0;
        for(int i=0; i<s.length(); i++) {
            sum += s.charAt(i) - '0';
        }
        return x % sum == 0;
    }
}
