import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		ArrayList<Integer>[] graph = new ArrayList[n+1];
		for(int i = 0 ; i < n+1 ; i ++) {
			graph[i] = new ArrayList<Integer>();
		}
		int[] indegree = new int[n+1];
		for(int i = 0 ; i < m ; i ++) {
			st = new StringTokenizer(br.readLine());
			int s = Integer.parseInt(st.nextToken());
			int e = Integer.parseInt(st.nextToken());
			graph[s].add(e);
			indegree[e] += 1;
			
		}
		Deque<Integer> q = new ArrayDeque<>();
		for(int i = 1 ; i < n+1 ; i ++) {
			if(indegree[i] == 0) {
				q.addLast(i);
			}
		}
		while(!q.isEmpty()) {
			int node = q.pollFirst();
			System.out.print(node + " ");
			for(int i = 0 ; i < graph[node].size(); i++) {
				int x = graph[node].get(i);
				indegree[x] -= 1;
				if (indegree[x] == 0 ) {
					q.addLast(x);
				}
			}
		}
		
		
	}

}