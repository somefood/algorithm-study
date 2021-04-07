import java.util.Scanner;

public class prac9498 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int num = scan.nextInt();
        if (num >= 90 && num <=100) System.out.print("A");
        else if (num >= 80 && num <=89) System.out.print("B");
        else if (num >= 70 && num <=79) System.out.print("C");
        else if (num >= 60 && num <=69) System.out.print("D");
        else System.out.print("F");
    }
}
