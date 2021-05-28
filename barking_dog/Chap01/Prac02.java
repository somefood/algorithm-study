public class Prac02 {
	static int func1(int n) {
		int sum = 0;
		for (int i = 1; i <= n; i++) {
			if (i % 3 == 0 || i % 5 == 0)
				sum += i;
		}
		return sum;
	}

	static int func2(int[] arr, int n) {
		for (int i = 0; i < n; i++) {
			for (int j = i + 1; j < n; j++) {
				if (arr[i] + arr[j] == 100)
					return 1;
			}
		}
		return 0;
	}

	static int func3(int n) {
		for (int i = 1; i * i <= n; i++) {
			if (i * i == n)
				return 1;
		}
		return 0;
	}
	
	static int func4(int n) {
		int i = 1;
		while(true) {
			if(i*2 <= n) i*=2;
			else break;
		}
		return i;
	}

	static void test1() {
		System.out.println("****** func1 test ******\n");
		int[] n = { 16, 34567, 27639 };
		int[] ans = { 60, 278812814, 178254968 };
		for (int i = 0; i < 3; i++) {
			int result = func1(n[i]);
			System.out.println("TC #" + i);
			System.out.println("expected : " + ans[i] + " result : " + result);
			if (ans[i] == result)
				System.out.println(" ... Correct!\n");
			else
				System.out.println(" ... Wrong!\n");
		}
		System.out.println("*************************\n\n");
	}

	static void test2() {
		int[][] arr = { { 1, 52, 48 }, { 50, 42 }, { 4, 13, 63, 87 } };
		int[] n = { 3, 2, 4 };
		int[] ans = { 1, 0, 1 };
		for (int i = 0; i < 3; i++) {
			int result = func2(arr[i], n[i]);
			System.out.println("TC #" + i);
			System.out.println("expected : " + ans[i] + "result : " + result);
			if (ans[i] == result)
				System.out.println("...Correct!");
			else
				System.out.println("...Wrong!");
		}
	}

	static void test3() {
		System.out.println("****** func3 test ******\n");
		int[] n = { 9, 693953651, 756580036 };
		int[] ans = { 1, 0, 1 };
		for (int i = 0; i < 3; i++) {
			int result = func3(n[i]);
			System.out.println("TC #" + i);
			System.out.println("expected : " + ans[i] + " result : " + result);
			if (ans[i] == result)
				System.out.println(" ... Correct!");
			else
				System.out.println(" ... Wrong!");
		}
		System.out.println("*************************\n");
	}

	static void test4() {
		System.out.println("****** func4 test ******\n");
		int[] n = { 5, 97615282, 1024 };
//		int[] n = { 5};
		int[] ans = { 4, 67108864, 1024 };
//		int[] ans = { 4};
		for (int i = 0; i < 3; i++) {
			int result = func4(n[i]);
			System.out.println("TC #" + i);
			System.out.println("expected : " + ans[i] + " result : " + result);
			;
			if (ans[i] == result)
				System.out.println(" ... Correct!");
			else
				System.out.println(" ... Wrong!");
			;
		}
		System.out.println("*************************\n");
		;
	}

	public static void main(String[] args) {
		test1();
		test2();
		test3();
		test4();
	}
}
