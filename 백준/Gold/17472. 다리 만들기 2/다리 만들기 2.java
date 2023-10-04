import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	static int n,m;
	static int[] dx = {0,0,1,-1};
	static int[] dy = {1,-1,0,0};
	static int[][] board;
	static ArrayDeque<int[]> q = new ArrayDeque<>();
	static int[] parents;
	static int[][] graph;
	
	static int find(int x) {
		if(x == parents[x]) return x;
		return parents[x] = find(parents[x]);
	}
	static boolean union(int a, int b) {
		int A = find(a);
		int B = find(b);
		if (A == B) return true;
		else parents[A] = B;
		return false;
	}
	
	static boolean check() {
		for(int i = 1; i< graph.length; i++) {
			for(int j = i; j < graph.length ; j++) {
				if(!union(i,j)) return true;
			}
		}
		
		return false;
	}
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		board = new int[n][m];
		for(int i = 0 ; i < n ; i ++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0 ; j < m ; j++) {
				board[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		int ans = 0;
		int cnt = 0;
		boolean[][] visited = new boolean[n][m];
		for(int i = 0 ; i < n ; i++) {
			for(int j = 0; j < m ; j++) {
				if(board[i][j] == 1 && !visited[i][j]) {
					cnt+= 1;
					visited[i][j] = true;
					q.add(new int[] {i,j});
					while(!q.isEmpty()) {
						int[] tmp = q.pollFirst();
						int x = tmp[0];
						int y = tmp[1];
						board[x][y] = cnt;
						for(int k = 0 ; k < 4 ; k++) {
							int nx = x + dx[k];
							int ny = y + dy[k];
							if(0<=nx && nx < n && 0 <= ny && ny < m && board[nx][ny] == 1 && !visited[nx][ny]) {
								q.addLast(new int[] {nx,ny});
								visited[nx][ny] = true;
							}
						}
					}
				}
			}
		}
		//cnt -> 섬의 갯수
		// graph : 인접행렬
		graph = new int[cnt+1][cnt+1];
		parents = new int[cnt+1];
		for(int i = 1 ; i < cnt+1 ; i ++) {
			parents[i] = i;
		}
		for(int i = 0 ; i < n ; i ++) {
			for(int j = 0 ; j < m ; j++) {
				if(board[i][j] != 0) {
					for(int k = 0 ; k < 4 ; k++) {
						int idx = 0;
						int nx = i + dx[k];
						int ny = j + dy[k];
						while (0<=nx && nx < n && 0 <= ny && ny < m) {
							if(board[nx][ny] == board[i][j]) break; // 같은 섬이면 다른 방향 탐색
							if(board[nx][ny] == 0) {
								idx += 1;
								nx += dx[k];
								ny += dy[k];
							}
							else if(board[nx][ny] != 0) { // 다른 섬을 만나면
								if(idx < 2) break; // 길이가 1이면 다른 방향 탐색
								else {
									int u = board[i][j];
									int v = board[nx][ny];
									if(graph[u][v] == 0) graph[u][v] = idx;
									else graph[u][v] = Math.min(graph[u][v], idx);
									break;
								}
							}
						}
					}
				}
			}
		}
		ArrayList<int[]> edgeList = new ArrayList<>(); 
		for(int i = 1; i< cnt+1 ; i++) {
			for(int j = 1 ; j < cnt + 1 ; j++) {
				if(graph[i][j] != 0) edgeList.add(new int[] {i,j,graph[i][j]});
			}
		}
		edgeList.sort((e1, e2) -> {
			return e1[2] - e2[2];
		});
		int edgeNum = 0;
		for(int[] edge : edgeList) {
			if(edgeNum == cnt -1) break;
			if(!union(edge[0],edge[1])) {
				edgeNum+=1;
				ans += edge[2];
			}
		}
		
		if(ans == 0 || check() ) System.out.println(-1);
		else System.out.println(ans);
	
	}

}