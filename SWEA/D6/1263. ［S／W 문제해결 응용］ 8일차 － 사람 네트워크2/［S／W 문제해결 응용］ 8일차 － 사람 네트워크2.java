import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
	static int N, dist[][];
	static int INF = 1000000000;
	static int[] CC;
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int T = Integer.parseInt(br.readLine());
		for(int t = 1 ; t <= T ; t ++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken());
			dist = new int[N][N];
			CC = new int[N];
			int ans = 0;
			for(int i = 0 ; i < N ; i ++) {
				for(int j = 0 ; j < N ; j++) {
					dist[i][j] = Integer.parseInt(st.nextToken());
					if(i != j && dist[i][j] == 0) dist[i][j] = INF;
				}
			}
			for(int k = 0 ; k < N ; k++) {
				for(int i = 0 ; i < N ; i++) {
					if(k == i) continue;
					for(int j = 0 ; j < N ; j++) {
						if(i == j || j == k ) continue;
						dist[i][j] = Math.min(dist[i][k] + dist[k][j], dist[i][j]);
					}
				}
			}
			for(int i = 0 ; i < N ; i++) {
				for(int j = 0 ; j < N ; j ++) {
					CC[i] += dist[i][j];
				}
				if(ans == 0) ans = CC[i];
				else ans = Math.min(CC[i], ans);
			}
			
			System.out.println("#" + t + " " + ans);
			
		}
	}
}