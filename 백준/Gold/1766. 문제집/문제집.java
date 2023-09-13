import java.io.*;
import java.util.*;
public class Main {
	static int n,m;
	static boolean[] visited;
	static Comparator<Integer> comp = new Comparator<Integer>() {
		@Override
		public int compare(Integer o1, Integer o2) {
			if (indegree[o1] == indegree[o2]) return o1 - o2;
			return indegree[o1] - indegree[o2];
		}
	};
	static PriorityQueue<Integer> pq = new PriorityQueue<>(comp);
	static int[] indegree;
	static LinkedList<Integer>[] graph;
	
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		indegree = new int[n+1];
		visited = new boolean[n+1];
		graph = new LinkedList[n+1];
		for(int i = 0 ; i < n ; i ++) {
			graph[i+1] = new LinkedList<Integer>();
		}
		
		for(int i = 0 ; i < m ; i ++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			indegree[b] += 1;
			graph[a].add(b);
		}
		
		for(int i = 1 ; i <= n ; i++) {
			if(indegree[i] == 0) pq.add(i);
		}
		while(!pq.isEmpty()) {
			int node = pq.poll();
			System.out.print(node + " ");
			while(!graph[node].isEmpty()) {
				int p = graph[node].poll();
				indegree[p] -= 1;
				if (indegree[p] == 0) pq.add(p);
			}
		}
	}
}