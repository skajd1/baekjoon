import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
// d : 1 2 3 4
//	   위 아래 오른 왼
public class Main {
	
	static class Shark{
		int x;
		int y;
		int v;
		int dir;
		int size;
		int index;
		Shark(int x, int y, int v,int dir,int size,int index){
			this.x = x;
			this.y = y;
			this.v = v;
			this.dir = dir;
			this.size = size;
			this.index = index;
		}
		void changeDir() {
			if (dir == 1) dir = 2;
			else if(dir == 2) dir = 1;
			else if(dir == 3) dir = 4;
			else if(dir == 4) dir = 3;
		}
		int[] move() {
			for (int i = 0; i < v; i++) {
		        x += delta[dir - 1][0];
		        y += delta[dir - 1][1];
		        // 벽을 넘어갈 경우 방향 변경
		        if (x < 0 || x >= r || y < 0 || y >= c) {
		            changeDir();
		            x += delta[dir - 1][0] * 2;
		            y += delta[dir - 1][1] * 2;
		        }
		    }
			return new int[] {x,y};
		}
	}
	
	static int[][] delta = {{-1,0},{1,0},{0,1},{0,-1}};
	static int r;
	static int c;
	static int m;
	static int ans;
	static Shark[][] board;

	static void move() {
		Shark[][] tmp = new Shark[r][c];
		for(int i = 0 ; i < r ; i ++) {
			for(int j = 0 ; j < c; j ++) {
				if(board[i][j] != null) {
					int[] moved = board[i][j].move();
					int x = moved[0];
					int y = moved[1];
					if(tmp[x][y] != null) {
						if(tmp[x][y].size > board[i][j].size) continue;
					}
					tmp[x][y] = board[i][j];
				}
			}
		}
		board = tmp;
	}
	static void kill(int y) {
	    for (int i = 0; i < r; i++) {
	        if (board[i][y] != null) { // 상어가 있으면 죽이기
	            ans += board[i][y].size;
	            board[i][y] = null;
	            break; // 1마리만 죽이기
	        }
	    }
	}
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		r = Integer.parseInt(st.nextToken());
		c = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		board = new Shark[r][c];
		ans = 0;
		for(int i = 0 ; i < m ; i ++) {
			st = new StringTokenizer(br.readLine());
			int rr = Integer.parseInt(st.nextToken());
			int cc = Integer.parseInt(st.nextToken());
			int s = Integer.parseInt(st.nextToken());
			int d = Integer.parseInt(st.nextToken());
			int z = Integer.parseInt(st.nextToken());
			board[rr-1][cc-1] = new Shark(rr-1,cc-1,s,d,z,i);
		}
		for(int t = 0 ; t < c ; t ++) {
			kill(t);
			move();
		}
		System.out.println(ans);
	}
}