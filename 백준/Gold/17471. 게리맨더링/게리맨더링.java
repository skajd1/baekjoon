import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
	static int n;
	static int[][] graph;
	static int[] p;
	static Deque<Integer> q = new ArrayDeque<>();
	
	static boolean isAdj(List<Integer> comb) {
		if(comb.size() == 1) return true;
		boolean[] visited = new boolean[n];
		int start = comb.get(comb.size()-1);
		q.addLast(start);
		while(!q.isEmpty()) {
			int node = q.pollFirst();
			for(int i = 1 ; i < n+1 ; i++) {
				if(graph[node][i] == 1 && comb.contains(i) && !visited[i-1]) {
					visited[i-1] = true;
					q.addLast(i);
				}
			}
		}
		for(int x : comb) {
			if (!visited[x-1]) return false;
		}
		return true;
	}
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		n = Integer.parseInt(br.readLine());
		st = new StringTokenizer(br.readLine());
		p = new int[n];
		for (int i = 0 ; i < n ; i ++) {
			p[i] = Integer.parseInt(st.nextToken());
		}
		graph = new int[n+1][n+1];
		int ans = 1000000000;
		for(int i = 1 ; i <= n ; i++) {
			st = new StringTokenizer(br.readLine());
			int num = Integer.parseInt(st.nextToken());
			for(int j = 0 ; j < num ; j ++) {
				graph[i][Integer.parseInt(st.nextToken())] = 1;
			}
		}
		for(int i = 2; i < (1<<n) ; i ++) {
			List<Integer> comb1 = new ArrayList<>();
			List<Integer> comb2 = new ArrayList<>();
			for(int j = 1 ; j <= n ; j ++) {
				if((i&(1<<j)) != 0) comb1.add(j);
				else comb2.add(j);
			}
			// 각 조합에서 서로 인접해 있는 상황이 아니면 continue
			// 인접해있으면 인구수 차이 계산
			if (isAdj(comb1) && isAdj(comb2)) {
				int tmp1 = 0;
				int tmp2 = 0;
				for(int x : comb1) tmp1+=p[x-1];
				for(int x : comb2) tmp2+=p[x-1];
				ans = Math.min(ans, Math.abs(tmp1-tmp2));
			}
		}
		if (ans ==1000000000) System.out.println(-1);
		else System.out.println(ans);
	}
}