import java.util.Scanner;

public class prac2884 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int a = scan.nextInt();
        int b = scan.nextInt();
        int c = b - 45;
        if (c <= -1) {
            if (a - 1 < 0) a = 23;
            else a -= 1;
            c += 60;
        }
        System.out.println(a+" "+c);
    }
}
