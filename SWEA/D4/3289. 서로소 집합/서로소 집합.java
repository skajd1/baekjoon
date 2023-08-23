import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
	
	static int[] parents;
	static int v;
	static int m;
	static void makeSet(){
		parents = new int[v+1];
		for (int i =1 ; i <= v ; i++){
			parents[i] = i;
		}
	}

	static int find(int a){
		if(parents[a] == a) return a;
		return parents[a] = find(parents[a]);
	}
	static void union(int a, int b){
		int rootA = find(a);
		int rootB = find(b);
		if (rootA > rootB) parents[rootA] = rootB;
		else parents[rootB] = rootA;
	}

	
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int T = Integer.parseInt(br.readLine());
		for(int i = 0 ; i < T ; i ++) {
			st = new StringTokenizer(br.readLine());
			StringBuilder sb = new StringBuilder();
			v = Integer.parseInt(st.nextToken());
			m = Integer.parseInt(st.nextToken());
			
			
			makeSet();
			for(int j = 0 ; j < m ; j ++) {
				st = new StringTokenizer(br.readLine());
				if (Integer.parseInt(st.nextToken()) == 1) {
					if (find(Integer.parseInt(st.nextToken())) == find(Integer.parseInt(st.nextToken()))) sb.append(1);
					else sb.append(0);
				}
				else {
					union(Integer.parseInt(st.nextToken()),Integer.parseInt(st.nextToken()));
				}
			}
			System.out.println("#"+ (i+1)+" " + sb);
			
		}
		
	}

}