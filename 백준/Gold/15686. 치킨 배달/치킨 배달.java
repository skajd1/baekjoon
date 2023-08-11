import java.util.LinkedList;
import java.util.List;
import java.util.Scanner;

public class Main {
	static int n;
	static int m;
	static int[][] city;
	static int ans;
	static boolean[] visited;
	static LinkedList<int[]> loc = new LinkedList<>();
	static int[][] candi;
	static int candiNum;
	static int getDist(int x, int y, List<int[]> loc) {
		int s = 1000000000;
		
		for(int[] l : loc) {
			s = Math.min(s, Math.abs(l[0]-x) + Math.abs(l[1]-y));
		}
		return s;
	}
	static void dfs(int N, int idx) {
		if (N == m) {
			int tmp = 0;
			for(int i = 0 ; i < n ; i ++) {
				for (int j = 0 ; j < n ; j ++) {
					if (city[i][j] == 1) {
						tmp += getDist(i,j,loc);
					}
				}
			}
			ans = Math.min(ans, tmp);
			return;
		}
		
		for(int i = idx; i < candi.length; i ++) {
			if(!visited[i]) {
				visited[i] = true;
				loc.add(new int[] {candi[i][0], candi[i][1]});
				dfs(N+1, i+1);
				visited[i] = false;
				loc.pollLast();
				
				
			}
		}
	
	}
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		n = sc.nextInt();
		m = sc.nextInt();
		city = new int[n][n];
		ans = 1000000000;
		for (int i = 0 ; i < n ; i ++) {
			for(int j = 0 ; j < n ; j ++) {
				city[i][j] = sc.nextInt();
				if (city[i][j] == 2) {
					candiNum += 1;
				}
			}
		}
		int tmp = 0;
		candi = new int[candiNum][2];
		for (int i = 0 ; i < n ; i ++) {
			for(int j = 0 ; j < n ; j ++) {
				if (city[i][j] == 2) {
					candi[tmp][0] = i;
					candi[tmp][1] = j;
					tmp++;
				}
			}
		}


		visited = new boolean[candi.length];
		dfs(0,0);
		
		System.out.println(ans);
		
	}
}