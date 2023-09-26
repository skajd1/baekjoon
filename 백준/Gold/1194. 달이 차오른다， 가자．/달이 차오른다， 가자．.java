import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.StringTokenizer;

public class Main {
	static int n,m;
	static ArrayDeque<int[]> q = new ArrayDeque<>();
	
	static int[] loc = {-1,-1};
	static int[] dx = {0,0,1,-1};
	static int[] dy = {1,-1,0,0};
	static char[][] board;
	static int ans = -1;
	static boolean[][][] visited;
	
	static void bfs() {
		visited = new boolean[64][n][m];
		q.add(new int[] {loc[0],loc[1],0,0});
		visited[0][loc[0]][loc[1]] = true;
		while(!q.isEmpty()) {
			int tmp[] = q.pollFirst();
			int x = tmp[0];
			int y = tmp[1];
			int dist = tmp[2];
			int keys = tmp[3];
			if (board[x][y] == '1') {
				if (ans == -1) ans = dist;
				ans = Math.min(ans, dist);
			}
			for(int i = 0 ; i < 4 ; i++) {
				int nx = x + dx[i];
				int ny = y + dy[i];
				if(0<=nx && nx < n && 0<=ny && ny < m && !visited[keys][nx][ny]) {
					if (board[nx][ny] == '#') continue;
					if(board[nx][ny] == '.' || board[nx][ny] == '0' || board[nx][ny] == '1') {
						q.addLast(new int[] {nx,ny,dist +1,keys});
					}
					else if(board[nx][ny] == 'a' || board[nx][ny] == 'b' || board[nx][ny] == 'c' || board[nx][ny] == 'd' || board[nx][ny] == 'e' || board[nx][ny] == 'f') {
						q.addLast(new int[] {nx,ny,dist+1,keys | 1 << (board[nx][ny] - 'a')});
					}
					else if(board[nx][ny] == 'A' || board[nx][ny] == 'B' || board[nx][ny] == 'C' || board[nx][ny] == 'D' || board[nx][ny] == 'E' || board[nx][ny] == 'F') {
						if ((int)Math.pow(2, board[nx][ny]-'A') == (keys & (1<<(board[nx][ny] - 'A')))) {
							q.addLast(new int[] {nx,ny,dist+1,keys});
						}
					}
					visited[keys][nx][ny] = true;
				}
			}
		}
	}
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		board = new char[n][m];
		for(int i = 0 ; i < n ; i++) {
			board[i] = br.readLine().toCharArray();
			if (loc[0] == -1) {
				for(int j = 0 ; j < m ; j++) {
					if(board[i][j] == '0') {
						loc[0] = i;
						loc[1] = j;
					}
				}
			}
		}
		bfs();
		System.out.println(ans);
	}

}