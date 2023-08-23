import java.util.*;
import java.io.*;
public class Solution {
	
	static int n;
	static int start;
	static int ans;
	static int maxDepth;
	static int[][] graph;
	static boolean[] visited;
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		for(int tc = 1; tc <= 10 ; tc ++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			n = Integer.parseInt(st.nextToken());
			start = Integer.parseInt(st.nextToken());
			graph = new int[100][100];
			visited = new boolean[100];
			ans = 0;
			maxDepth = 0;
			st = new StringTokenizer(br.readLine());
			for(int i = 0 ; i < n/2 ; i ++) {
				int s = Integer.parseInt(st.nextToken());
				int e = Integer.parseInt(st.nextToken());
				graph[s-1][e-1] = 1;
			}
			Deque<int[]> q = new ArrayDeque<>();
			q.offerLast(new int[] {start,0});
			visited[start-1] = true;
			while(!q.isEmpty()) {
				int[] tmp = q.pollFirst();
				int node = tmp[0];
				int depth = tmp[1];
				if(maxDepth < depth) {
					maxDepth = depth;
					ans = node;
				}
				else if(maxDepth == depth) ans = Math.max(ans, node);
				for(int i =0 ; i < 100 ; i ++) {
					if (graph[node-1][i] == 1 && !visited[i]) {
						visited[i] = true;
						q.offerLast(new int[] {i+1, depth+1});
					}
				}
			}
			System.out.println("#" + tc + " " + ans);
		}
	}
}