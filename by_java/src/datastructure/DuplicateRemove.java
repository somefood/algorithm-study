package datastructure;

import java.util.LinkedHashSet;

public class DuplicateRemove {

    public static void main(String[] args) {
        int[] list = {1, 1, 1, 2, 2, 4, 4, 4, 3, 5, 4, 1, 2, 3};
        LinkedHashSet<Integer> hashSet = new LinkedHashSet<>();

        for (int i : list) {
            hashSet.add(i);
        }

        System.out.println(hashSet);
    }
}
