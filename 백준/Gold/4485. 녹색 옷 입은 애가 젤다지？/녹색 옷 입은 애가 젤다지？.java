import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.StringTokenizer;

public class Main {
	static int N, board[][],distance[][];
	static int[] dx = {0,0,1,-1};
	static int[] dy = {1,-1,0,0};

	static void dijkstra() {
		ArrayDeque<int[]> q = new ArrayDeque<>();
		q.add(new int[] {0,0});
		while(!q.isEmpty()) {
			int[] tmp = q.pollFirst();
			int x = tmp[0];
			int y = tmp[1];
			for(int i = 0 ; i < 4 ; i ++) {
				int nx = x + dx[i];
				int ny = y + dy[i];
				if(0<=nx && nx < N && 0<= ny && ny < N) {
					if(distance[nx][ny] > distance[x][y] + board[nx][ny]) {
						q.add(new int[] {nx,ny});
						distance[nx][ny] = distance[x][y] + board[nx][ny];
					}
				}
			}
		}
	}
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int t = 0;
		while (true) {
			t += 1;
			st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken());
			if(N == 0) break;
			board = new int[N][N];
			distance = new int[N][N];
			for(int i = 0 ; i < N ; i++) {
				st = new StringTokenizer(br.readLine());
				for(int j = 0 ; j < N ; j++) {
					board[i][j] = Integer.parseInt(st.nextToken());
					distance[i][j] = 100000000;
				}
			}
			distance[0][0] = board[0][0];
			dijkstra();
			System.out.println("Problem " + t + ": " + distance[N-1][N-1]);
		}
	}
}