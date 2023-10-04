import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class Solution {
	static int n,m;
	static LinkedList<Integer>[] indegree;
	static LinkedList<Integer>[] outdegree;
	static ArrayDeque<Integer> q = new ArrayDeque<>();
	static int func(int node) {
		int result = 0;
		boolean[] visited = new boolean[n+1];
		q.add(node);
		visited[node] = true;
		while(!q.isEmpty()) {
			int now = q.pollFirst();
			for(int in : indegree[now]) {
				if(!visited[in]) {
					visited[in] = true;
					q.addLast(in);
					result += 1;
				}
			}
		}
		q.add(node);
		visited[node] = true;
		visited = new boolean[n+1];
		while(!q.isEmpty()) {
			int now = q.pollFirst();
			for(int out : outdegree[now]) {
				if(!visited[out]) {
					visited[out] = true;
					q.addLast(out);
					result += 1;
				}
			}
		}
		return result;
	}

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int T = Integer.parseInt(br.readLine());
		for(int t = 1 ; t <= T ; t ++) {
			n = Integer.parseInt(br.readLine());
			m = Integer.parseInt(br.readLine());
			indegree = new LinkedList[n+1];
			outdegree = new LinkedList[n+1];
			for(int i = 0 ; i <= n ; i++) {
				indegree[i] = new LinkedList<>();
				outdegree[i] = new LinkedList<>();
			}
			int ans = 0;
			for(int i = 0 ; i < m ; i++) {
				StringTokenizer st = new StringTokenizer(br.readLine());
				int a = Integer.parseInt(st.nextToken());
				int b = Integer.parseInt(st.nextToken());
				indegree[b].add(a);
				outdegree[a].add(b);
			}
			for(int i = 1 ; i <= n ; i++) {
				if(func(i) == n-1) ans += 1;
			}
			System.out.println("#" + t + " " + ans);
		}
	}

}