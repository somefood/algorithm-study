import java.util.Scanner;

public class prac2588 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int a = scan.nextInt();
        int b = scan.nextInt();
        System.out.println(a * (b%10));
        System.out.println(a * (int)((b % 100 / 10)));
        System.out.println(a * (int)((b/100)));
        System.out.println(a * b);
    }
}
