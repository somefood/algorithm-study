package programmers;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class 전화번호목록 {
    public boolean solution(String[] phone_book) {
        boolean answer = true;
        Arrays.sort(phone_book);
        System.out.println(Arrays.toString(phone_book));
        HashMap<String, Integer> hashMap = new HashMap<>();
        for (int i = 0; i < phone_book.length; i++) {
            hashMap.put(phone_book[i], i);
        }
        for (int i = 0; i < phone_book.length; i++) {
            for (int j = 0; j < phone_book[i].length(); j++) {
                if (hashMap.containsKey(phone_book[i].substring(0, j)))
                    return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        전화번호목록 test = new 전화번호목록();
//        System.out.println(test.solution(new String[]{"1", "12"}));
        System.out.println(test.solution(new String[]{"12", "345", "1"}));
//        System.out.println(test.solution(new String[]{"119", "97674223", "1195524421"}));
//        System.out.println(test.solution(new String[]{"123", "456", "789"}));
//        System.out.println(test.solution(new String[]{"12", "123", "1235", "567", "88"}));
    }
}
