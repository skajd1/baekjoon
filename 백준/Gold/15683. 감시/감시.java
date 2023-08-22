import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	static int n;
	static int m;
	static int[][] Room;
	static int[][] delta = {{-1,0},{0,1},{1,0},{0,-1}};
	static int[][] direction1 = {{0},{1},{2},{3}};
	static int[][] direction2 = {{0,2},{1,3}};
	static int[][] direction3 = {{0,1},{1,2},{2,3},{3,0}};
	static int[][] direction4 = {{0,1,2},{1,2,3},{2,3,0},{3,0,1}};
	static int[][] direction5 = {{0,1,2,3}};
	static int ans;

	static int getSagak(int[][] room) {
		int tmp = 0;
		for(int i = 0 ; i < n ; i++) {
			for(int j = 0 ; j < m ; j ++) {
				if(room[i][j] == 0) {
					tmp++;
				}
			}
		}
		return tmp;
	}
	static void changeRoom(int[] dir, int x, int y, int[][] room) {
		int changed = 0;
		for(int d : dir) {
			int cnt = 1;
			while(true) {
				int nx = x + delta[d][0]*cnt;
				int ny = y + delta[d][1]*cnt;
				if(0<=nx && nx < n && 0<=ny && ny < m && (room[nx][ny] != 6 )) {
					if(room[nx][ny] == 0) {
						changed += 1;
						room[nx][ny] = -1;	
					}
					cnt += 1;
				}
				else break;
			}
		}
	}
	static void init(int[][] room_copy, int[][] room) {
		for(int i = 0 ; i < n ; i ++) {
			for(int j = 0 ; j < m ; j++) {
				room_copy[i][j] = room[i][j];
			}
		}
	}
	static void dfs(int x, int y, int[][] room) {
		if(x == n) { // 전체 탐색 완료 후 ans 계산
			ans = Math.min(ans, getSagak(room));
			return;
		}
		if(y == m) { // 다음 행
			dfs(x+1,0,room);
			return;
		}
		int[][] room_copy = new int[n][m];
		
		if(room[x][y] == 1) {
			for(int i = 0 ; i < 4 ; i ++) {
				init(room_copy, room);
				changeRoom(direction1[i],x,y,room_copy);
				dfs(x,y+1,room_copy);
			}
		}
		else if(room[x][y] == 2) {
			for(int i = 0 ; i < 2 ; i ++) {
				init(room_copy, room);
				changeRoom(direction2[i],x,y,room_copy);
				dfs(x,y+1,room_copy);
			}			
		}
		else if(room[x][y] == 3) {
			for(int i = 0 ; i < 4 ; i ++) {
				init(room_copy, room);
				changeRoom(direction3[i],x,y,room_copy);
				dfs(x,y+1,room_copy);
			}
		}
		else if(room[x][y] == 4) {
			for(int i = 0 ; i < 4 ; i ++) {
				init(room_copy, room);
				changeRoom(direction4[i],x,y,room_copy);
				dfs(x,y+1,room_copy);
			}
		}
		else if(room[x][y] == 5) {
			init(room_copy, room);
			changeRoom(direction5[0],x,y,room_copy);
			dfs(x,y+1,room_copy);
		}
		else dfs(x,y+1,room);
	}
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		Room = new int[n][m];
		for (int i = 0 ; i < n ; i ++) {
			st = new StringTokenizer(br.readLine());
			for(int j = 0 ; j < m ; j ++) {
				Room[i][j] = Integer.parseInt(st.nextToken()); 
			}
		}
		ans = n*m;
		dfs(0,0,Room);
		System.out.println(ans);
    }
}