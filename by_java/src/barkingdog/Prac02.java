package barkingdog;

public class Prac02 {
    static int func2(int[] arr, int n) {
        int[] result = new int[101];
        for(int i=0; i<n; i++) {
            if(result[100-arr[i]] == 1)
                return 1;
            result[arr[i]] = 1;
        }
        return 0;
    }

    public static void main(String[] args) {
        System.out.println(func2(new int[]{1, 52, 48}, 3));
        System.out.println(func2(new int[]{50, 42}, 2));
        System.out.println(func2(new int[]{4, 13, 63, 87}, 4));
    }
}
