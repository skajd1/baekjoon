import java.util.ArrayList;
import java.util.Scanner;

public class Main {
	static ArrayList<Integer> candidate = new ArrayList<>();
	static boolean[] visited;
	static int[] sins;
	static int[] ssns;
	static int N;
	static void subset(int cnt) {
		if (cnt == N) {
			int sin = 1;
			int ssn = 0;
			boolean check = false;
			for(int i = 0 ; i < N ; i++) {
				if (visited[i]) {
					sin *= sins[i];
					ssn += ssns[i];
					check = true;
				}
			}
			if(check) candidate.add(Math.abs(sin-ssn));
			return;
		}
		visited[cnt] = true;
		subset(cnt+1);
		visited[cnt] = false;
		subset(cnt+1);
	}
	public static void main(String[] args) {
		Scanner sc  = new Scanner(System.in);
		N = sc.nextInt();
		sins = new int[N];
		ssns = new int[N];

		visited = new boolean[N];
		for(int i = 0 ; i < N ; i ++) {
			sins[i] = sc.nextInt();
			ssns[i] = sc.nextInt();
		}
		subset(0);
		int min = 1000000000;
		for(int x : candidate) {
			if (min >= x) {
				min = x;
			}
		}
		System.out.println(min);
		

	}
}