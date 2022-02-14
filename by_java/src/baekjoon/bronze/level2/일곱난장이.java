package baekjoon.bronze.level2;

import java.util.*;

public class 일곱난장이 {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int[] list = new int[9];
        List<Integer> results = new ArrayList<>();

        for(int i=0; i<list.length; i++) {
            list[i] = scanner.nextInt();
        }

        Arrays.sort(list);

        int idx = 0;
        while(idx != -1) {
            int sum = 0;
            for(int i=0; i< list.length; i++) {
                sum = list[i];
                results.add(list[i]);
                for(int j=i+1; j<list.length; j++) {
                    sum += list[j];
                    results.add(list[j]);
                    if (sum == 100 && results.size() == 7) {
                        idx = -1;
                        break;
                    }
                }
            }
        }
        System.out.println(results);
    }
}
