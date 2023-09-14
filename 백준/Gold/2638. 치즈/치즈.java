import java.io.*;
import java.util.*;
public class Main {
	static int n,m;
	static int[][] board;
	static int ans;
	static int[] dx = {1,-1,0,0};
	static int[] dy = {0,0,1,-1};
	static boolean[][] air;
	static LinkedList<int[]> li = new LinkedList<>();

	//치즈가 있으면 true 반환
	static boolean isEmpty() {
		boolean res = true;
		for(int i = 0 ; i < n ; i ++ ) {
			for(int j = 0 ; j < m ; j++) {
				if(board[i][j] == 1) return false;
			}
		}
		return res;
	}
	// x,y가 outside인지 체크
	static boolean isOutside(int x, int y) {
		boolean res = false;
		int cnt = 0;
		for(int i = 0 ; i < 4 ; i++) {
			int nx = x + dx[i];
			int ny = y + dy[i];
			if(board[nx][ny] == 0 && air[nx][ny]) {
				cnt += 1;
			}
			if (cnt == 2) return true;
		}
		return res;
	}
	//녹이는 함수
	static void melt() {
		initAir();
		for(int i = 0 ; i < n ; i++) {
			for(int j = 0 ; j < m ; j++) {
				if(board[i][j] == 1 && isOutside(i,j)) {
					li.add(new int[] {i,j});
				}
			}
		}
		while(!li.isEmpty()) {
			int[] tmp = li.poll();
			board[tmp[0]][tmp[1]] = 0;
		}
		ans += 1;
	}
	// 바깥 공기 인지 판별
	static void initAir() {
		air = new boolean[n][m];
		
		ArrayDeque<int[]> q = new ArrayDeque<>();
		q.add(new int[] {0,0});
		air[0][0] = true;
		while(!q.isEmpty()) {
			int[] tmp = q.pollFirst();
			int x = tmp[0];
			int y = tmp[1];
			for(int i = 0 ; i < 4 ; i ++) {
				int nx = x + dx[i];
				int ny = y + dy[i];
				if(0<=nx && nx < n && 0<=ny && ny < m && !air[nx][ny] && board[nx][ny] == 0){
					q.addLast(new int[] {nx,ny});
					air[nx][ny] = true;
				}
			}
		}
		
	}
	
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		board = new int[n][m];
		for(int i = 0 ; i < n ; i++) {
			st = new StringTokenizer(br.readLine());
			for(int j = 0 ; j < m ; j++) {
				board[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		while(!isEmpty()) {
			melt();
		}
		System.out.println(ans);		
	}
}