import java.util.Scanner;

public class prac14681 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int a = scan.nextInt();
        int b = scan.nextInt();
        if (a >= 1 && b >= 1) System.out.println(1);
        else if (a <= -1 && b >= 1) System.out.println(2);
        else if (a <= -1 && b <= -1) System.out.println(3);
        else System.out.println(4);
    }
}
