import java.io.*;
import java.util.*;

public class Solution {
	static int n,m,k,ans;
	static int[][] board;
	static int[] dx = {0,0,1,-1};
	static int[] dy = {1,-1,0,0};
	static LinkedList<Integer> order = new LinkedList<>();
	static ArrayDeque<int[]> q = new ArrayDeque<>();
	
	static void copy(int[][] copied) {
		for(int i = 0 ; i < n ; i++) {
			for(int j = 0 ; j < m ; j++) {
				copied[i][j] = board[i][j];
			}
		}
	}
	static void dfs(int cnt) {
		if(cnt == k) {
			int[][] copied = new int[n][m];
			copy(copied);
			for (int y : order) {
				delete(y,copied);
				drop(copied);
			}
			ans = Math.min(ans, getBlocks(copied));
			return;
		}
		for(int i = 0 ; i < m ; i++) {
			order.addLast(i);
			dfs(cnt+1);
			order.pollLast();
		}
	}
	static void delete(int y, int[][] copied) {
		//반응한 벽돌 q에 넣고 지우기
		boolean[][] visited = new boolean[n][m];
		for(int x = 0 ; x < n ; x++) {
			if(copied[x][y] != 0) {
				visited[x][y] = true;
				q.add(new int[] {x,y});
				while(!q.isEmpty()) {
					int[] tmp = q.pollFirst();
					int xx = tmp[0];
					int yy = tmp[1];
					int range = copied[xx][yy];
					copied[xx][yy] = 0;
					for(int k = 0 ; k < 4 ; k++) {
						for(int r = 1 ; r < range ; r ++) {
							int nx = xx + dx[k]*r;
							int ny = yy + dy[k]*r;
							if(0<=nx && nx< n && 0<=ny && ny < m && !visited[nx][ny] && copied[nx][ny] > 0) {
								visited[nx][ny] = true;
								q.add(new int[] {nx,ny});
							}
						}
					}
				}
				break;
			}
		}
	}
	static void drop(int[][] copied) {
		for(int j = 0; j < m ; j++) {
			for(int i = n-2 ; i > -1 ; i--) {
				if(copied[i][j] == 0) continue;
				int cnt = i;
				int tmp = copied[i][j];
				while(cnt+1 < n && copied[cnt+1][j] == 0) cnt +=1;
				copied[i][j] = 0;
				copied[cnt][j] = tmp;
			}
		}
	}
	static int getBlocks(int[][] copied) {
		int blocks = 0;
		for(int i = 0 ; i < n ; i++) {
			for(int j = 0 ; j < m ; j++) {
				if(copied[i][j] != 0) blocks++;
			}
		}
		return blocks;
	}
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int T = Integer.parseInt(st.nextToken());
		for(int t = 1; t <= T ; t ++) {
			ans = 9999999;
			st = new StringTokenizer(br.readLine());
			k = Integer.parseInt(st.nextToken());
			m = Integer.parseInt(st.nextToken());
			n = Integer.parseInt(st.nextToken());
			board = new int[n][m];
			for(int i = 0 ; i < n ; i++) {
				st = new StringTokenizer(br.readLine());
				for(int j = 0 ; j < m ; j++) {
					board[i][j] = Integer.parseInt(st.nextToken());
				}
			}
			dfs(0);
			System.out.println("#" + t + " " + ans);
		}
	}
}