import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.LinkedList;
import java.util.StringTokenizer;
public class Main {
	static int n,m,ans,cheese,pre_cheese;
	static int[] dx = {1,-1,0,0};
	static int[] dy = {0,0,1,-1};
	static int[][] board;
	static LinkedList<int[]> li = new LinkedList<>();
	static ArrayDeque<int[]> q = new ArrayDeque<>(); 
	
	static void melt() {
		pre_cheese = cheese;
		boolean[][] visited = new boolean[n][m];
		visited[0][0] = true;
		q.add(new int[] {0,0});
		while(!q.isEmpty()) {
			int[] tmp = q.pollFirst();
			for(int i = 0 ; i < 4 ; i ++) {
				int nx = tmp[0] + dx[i];
				int ny = tmp[1] + dy[i];
				if(0<=nx&&nx<n && 0<=ny&&ny<m &&!visited[nx][ny]) {
					visited[nx][ny] = true;
					if(board[nx][ny] == 0) q.addLast(new int[] {nx,ny});
					else li.add(new int[] {nx,ny});
				}
			}
		}
		while(!li.isEmpty()) {
			int[] tmp = li.poll();
			board[tmp[0]][tmp[1]] = 0;
			cheese-=1;
		}
		ans += 1;
	}

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		board = new int[n][m];
		for(int i = 0 ; i < n ; i ++) {
			st = new StringTokenizer(br.readLine());
			for(int j = 0 ; j < m ; j ++) {
				board[i][j] =Integer.parseInt(st.nextToken());
				if (board[i][j] == 1) cheese += 1;
			}
		}
		while(cheese > 0) melt();
		
		System.out.println(ans + "\n" + pre_cheese);
	}
}