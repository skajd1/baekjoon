import java.util.Scanner;

public class Main {
	static int N,M;
	static int[] num;
	static boolean[] visited;
	public static void perm(int depth) {
		if (depth == 0) {
			for(int i = 0 ; i < M ; i ++) {
				System.out.print(num[i] + " ");
			}
			System.out.println();
			return;
		}
		
		for(int i = 1 ; i <= N ; i ++) {
			if (!visited[i-1]) {
				visited[i-1] = true;
				num[M-depth] = i;
				perm(depth-1);
				visited[i-1] = false;
			}
		}
	}
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N =sc.nextInt();
		M = sc.nextInt();
		visited = new boolean[N];
		num = new int[M];
		perm(M);
		

	}

}
