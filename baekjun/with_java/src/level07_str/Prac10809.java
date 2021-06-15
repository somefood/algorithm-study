package level07_str;

import java.util.Scanner;

public class Prac10809 {
    public static void main(String[] args) {
        String s = new Scanner(System.in).next();
        int[] index = new int[26];
        for(int i=0; i<index.length; i++) {
            index[i] = -1;
        }
        for(int i=0; i<s.length(); i++) {
            char c = s.charAt(i);
            if(index[c-'a'] > -1) continue;
            index[c-'a'] = i;
        }

        for(int i=0; i<index.length; i++) {
            System.out.print(index[i] + " ");
        }
    }
}
