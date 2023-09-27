import java.util.Arrays;
import java.util.Scanner;

public class Main {
	static int N,M, dist[][];
	static int INF = 1000000000;
	public static void main(String[] args) {
		Scanner sc  = new Scanner(System.in);
		N = sc.nextInt();
		M = sc.nextInt();
		dist = new int[N][N];
		
		for(int i = 0 ; i < M ; i++) {
			int u = sc.nextInt();
			int v = sc.nextInt();
			int c = sc.nextInt();
			if(dist[u-1][v-1]  == 0) dist[u-1][v-1] = c;
			else dist[u-1][v-1] = Math.min(dist[u-1][v-1], c);
		}
		for(int i = 0 ; i < N ; i++) {
			for(int j = 0 ; j < N  ; j++) {
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
			for(int j = 0 ; j < N ; j++) {
				if(dist[i][j] == INF) dist[i][j] = 0;
				System.out.print(dist[i][j]+ " ");
			}
			System.out.println();
		}
		
	}

}