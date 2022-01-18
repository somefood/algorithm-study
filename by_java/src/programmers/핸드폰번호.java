package programmers;

public class 핸드폰번호 {
    public static String solution(String phone_number) {
        StringBuilder answer = new StringBuilder();
        for(int i=0; i<phone_number.length()-4; i++) {
            answer.append("*");
        }
        for(int i=phone_number.length()-4; i<phone_number.length(); i++) {
            answer.append(phone_number.charAt(i));
        }
        return answer.toString();
    }

    public static void main(String[] args) {
        System.out.println(solution("01012345678"));
        System.out.println(solution("021234567"));
    }
}
