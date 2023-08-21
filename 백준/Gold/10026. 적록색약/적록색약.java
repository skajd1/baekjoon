import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;

public class Main {	
	static int n;
	static char[][] img;
	static boolean[][] visited1;
	static boolean[][] visited2;
	static int[] dx = {0,0,1,-1};
	static int[] dy = {1,-1,0,0};
	static Deque<int[]> q;
	static void bfs1(char color) {
		while(!q.isEmpty()) {
			int[] xy = q.pollFirst();
			int x = xy[0];
			int y = xy[1];
			for(int k = 0 ; k < 4 ; k ++) {
				int nx = x + dx[k];
				int ny = y + dy[k];
				if(0<=nx && nx < n && 0<=ny && ny < n && !visited1[nx][ny] && img[nx][ny] == color) {
					visited1[nx][ny] = true;
					q.addLast(new int[] {nx,ny});
				}	
			}
		}	
	}
	static void bfs2(char color) {
		while(!q.isEmpty()) {
			int[] xy = q.pollFirst();
			int x = xy[0];
			int y = xy[1];
			for(int k = 0 ; k < 4 ; k ++) {
				int nx = x + dx[k];
				int ny = y + dy[k];
				if(0<=nx && nx < n && 0<=ny && ny < n && !visited2[nx][ny]) {
					if (color == 'R' || color == 'G') {
						if(img[nx][ny] == 'R' || img[nx][ny] == 'G') {
							visited2[nx][ny] = true;
							q.addLast(new int[] {nx,ny});							
						}
					}
					else {
						if(img[nx][ny] == color) {
							visited2[nx][ny] = true;
							q.addLast(new int[] {nx,ny});							
						}
					}
				}	
			}
		}	
	}
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		n = Integer.parseInt(br.readLine());
		img = new char[n][];
		for(int i = 0 ; i < n ; i ++) {
			img[i] = br.readLine().trim().toCharArray(); 
		}
		visited1= new boolean[n][n];  
		visited2= new boolean[n][n];  
		int ans1 = 0; //적록 x
		int ans2 = 0; //적록 o
		q = new ArrayDeque<>();
		for(int i = 0 ; i < n ; i ++) {
			for(int j = 0 ; j < n ; j ++) {
				if(!visited1[i][j]) {
					visited1[i][j] = true;
					q.addLast(new int[] {i,j});
					ans1 += 1;
					bfs1(img[i][j]);
				
				}
				if(!visited2[i][j]) {
					visited2[i][j] = true;
					q.addLast(new int[] {i,j});
					ans2 += 1;
					bfs2(img[i][j]);
				}
			}
		}
		System.out.println(ans1 + " " + ans2);
	}
}