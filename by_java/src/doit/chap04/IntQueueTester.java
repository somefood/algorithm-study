package doit.chap04;

import java.util.Scanner;

public class IntQueueTester {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        IntQueue s = new IntQueue(64);

        while (true) {
            System.out.println("현재 데이터 수 : " + s.size() + " /" + s.capacity());
            System.out.print("(1)푸시 (2)팝 (3)피크 (4) 덤프 (0) 종료 :");
            int menu = scanner.nextInt();
            if (menu == 0) break;

            int x;
            switch (menu) {
                case 1:
                    System.out.print("데이터: ");
                    x = scanner.nextInt();
                    try {
                        s.enque(x);
                    } catch (IntQueue.OverflowIntQueueException e) {
                        System.out.println("큐이 가득 찼다.");
                    }
                    break;

                case 2:
                    try {
                        x = s.deque();
                        System.out.println("팝한 데이터는 " + x + "이다.");
                    } catch (IntQueue.EmptyIntQueueException e) {
                        System.out.println("큐이 비어 있다.");
                    }
                    break;

                case 3:
                    try {
                        x = s.peek();
                        System.out.println("피크한 데이터는 " + x + "이다.");
                    } catch (IntStack.EmptyIntStackException e) {
                        System.out.println("큐이 비어 있다.");
                    }
                    break;

                case 4:
                    s.dump();
                    break;
            }
        }
    }
}
