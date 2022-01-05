package programmers;

public class 큰수만들기 {
    public static String solution(String number, int k) {
        StringBuilder sb = new StringBuilder();
        int index = 0;
        int max = 0;
        for(int i=0; i<number.length() - k; i++) {
            max = 0;
            for(int j = index; j<= k+i; j++) {
                if(max < number.charAt(j)-'0') {
                    max = number.charAt(j)-'0';
                    index = j+1;
                }
            }
            sb.append(max);
        }
        return sb.toString();
    }

    public static void main(String[] args) {
        System.out.println(solution("1924", 2));
        System.out.println(solution("123456789", 3));
        System.out.println(solution("4177252841", 4));
    }
}
