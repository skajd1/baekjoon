import java.util.Arrays;
import java.util.Scanner;

/// 높이 정렬 후
/// 제일 낮은 먹이부터 먹기

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int l = sc.nextInt();
		int[] height = new int[n];
		for (int i = 0 ; i < n ;  i++) {
			height[i] = sc.nextInt();
		}
		Arrays.sort(height);
		for(int h : height) {
			if (l >= h) l++;
			else break;
		}
		System.out.println(l);
	}

}