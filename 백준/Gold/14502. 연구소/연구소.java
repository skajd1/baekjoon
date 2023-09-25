import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.StringTokenizer;

public class Main {
	static int n , m;
	static int[][] board;
	static boolean[][] visited;
	static ArrayDeque<int[]> q = new ArrayDeque<>();
	static int[] dx = {1,-1,0,0};
	static int[] dy = {0,0,1,-1};
	static int ans;
	
	static int[][] copy(int[][] b){
		int[][] copied = new int[n][m];
		for(int i = 0 ; i < n ; i++) {
			for(int j = 0 ; j < m ; j++) {
				copied[i][j] = b[i][j];
			}
		}
		return copied;
		
	}
	static void infect(int x, int y, int[][] b){
		
		
		q.add(new int[] {x,y});
		visited[x][y] = true;
		while(!q.isEmpty()) {
			int[] tmp = q.pollFirst();
			int xx = tmp[0];
			int yy = tmp[1];
			for(int i = 0 ; i < 4 ; i++) {
				int nx = xx + dx[i];
				int ny = yy + dy[i];
				if(0<=nx && nx < n && 0<= ny && ny < m && b[nx][ny] == 0) {
					b[nx][ny] = 2;
					visited[nx][ny] = true;
					q.addLast(new int[] {nx,ny});
				}
			}
		}
		
	}
	
	static int getArea(int[][] b) {
		int result = 0;
		for(int i = 0 ; i < n ; i++) {
			for(int j = 0 ; j < m ; j++) {
				if(b[i][j] == 0) result += 1;
			}
		}
		return result;
	}
	static void dfs(int x, int y, int[][] b,int cnt) {
		if(cnt == 3) {
			int[][] copied = copy(b);
			visited = new boolean[n][m];
			for(int i = 0 ; i < n ; i++) {
				for(int j = 0 ; j < m ; j++) {
					if (b[i][j] == 2) {
						if (!visited[i][j])
							infect(i,j,copied);
					}
				}
			}
			ans = Math.max(getArea(copied),ans);
			return;
			
		}
		if(x == n) {
			return;
		}
		if(y == m) {
			dfs(x+1,0,b,cnt);
			return;
		}
		if(b[x][y] == 0) {
			b[x][y] = 1;
			dfs(x,y+1,b,cnt+1);
			b[x][y] = 0;
		}
		dfs(x,y+1,b,cnt);
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		board = new int[n][m];
		for(int i = 0; i < n ; i++){
			st = new StringTokenizer(br.readLine());
			for(int j = 0 ; j < m ; j++) {
				board[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		dfs(0,0,board,0);
		System.out.println(ans);
	}

}