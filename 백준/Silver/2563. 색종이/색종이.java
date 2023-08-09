import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int[][] paper = new int[100][100];
		int[][] loc = new int[n][2];
		for (int i = 0 ; i < n ; i ++) {
			loc[i][0] = sc.nextInt();
			loc[i][1] = sc.nextInt();
		}
		sc.close();
		
		for(int[] l : loc) {
			int x = l[0];
			int y = l[1];
			for(int i = x; i <x + 10; i ++) {
				for(int j = y; j < y+10; j ++) {
					paper[i][j] = 1;
				}
			}
		}
		int ans = 0 ;
		for(int[] x : paper) {
			for(int y : x) {
				if (y == 1) ans += 1;
			}
		}
		System.out.println(ans);
	}
		

}