package level06_function;

public class Prac4673 {
    static int[] selfNumber(int n) {
        int[] arr = new int[n];
        int[] arr2 = new int[n];
        int value;
        for(int i=0, j=1; i<n; i++, j++) {
            arr[i] = j;
            arr2[i] = j;
        }
        for(int i=0; i<n; i++) {
            int result = arr[i];
            String str = String.valueOf(arr[i]);
            for(int j=0; j<str.length(); j++) {
                result += str.charAt(j) - '0';
            }
            if (result <= 10000) {
                arr2[result-1] = 0;
            }
        }
        return arr2;
    }
    public static void main(String[] args) {
        int[] arr = selfNumber(10000);
        for(int i=0; i<10000; i++) {
            if(arr[i] != 0) System.out.println(arr[i]);
        }
    }
}
