import java.util.Scanner;

public class Main {
	static int N,M;
	static int[] num;
	public static void comb(int depth,int cnt) {
		if (depth == 0) {
			for(int i = 0 ; i < M ; i ++) {
				System.out.print(num[i] + " ");
			}
			System.out.println();
			return;
		}
		
		for(int i = cnt ; i <= N ; i ++) {
			
			num[M-depth] = i;
			comb(depth-1, i+1);
				
			
		}
	}
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N =sc.nextInt();
		M = sc.nextInt();
		num = new int[M];
		comb(M,1);
		

	}

}
