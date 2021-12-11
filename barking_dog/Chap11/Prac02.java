public class Prac02 {
    long POW(long a, long b, long m){
        if (b == 1) return a % m;
        long val = POW(a, b/2, m);
        val = val * val % m;
        if(b%2 == 0) return val;
        return val * a % m;
    }

    public static void main(String[] args) {
        System.out.println(POW(12, 58, 7));
    }
}