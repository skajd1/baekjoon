import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Deque;
import java.util.LinkedList;
import java.util.StringTokenizer;
/// 우선순위 : 아래 -> 왼쪽
/// 조합으로 궁수 자리 정하기
public class Main {
	
	static int n;
	static int m;
	static int d;
	static int[][] map;
	static int[][] map_copy;
	static int[] dx = {0,-1,0};
	static int[] dy = {-1,0,1};
	
	
	static void init() {
		for(int i = 0 ; i < n ; i ++) {
			for(int j = 0 ; j < m ; j ++) {
				map[i][j] = map_copy[i][j];
			}
		}
		
	}
	static void move() {
		for(int i = 0; i < m ; i++) {
			if (map[n-1][i] == 1) map[n-1][i] = 0;
		}
		for(int i = n-1 ; i >0 ; i--) {
			for(int j = 0 ; j < m ; j ++) {
				if (map[i-1][j] == 1) {
					map[i-1][j] = 0;
					map[i][j] = 1;
				}
			}
		}
		
	}
	static int attack(int[] archers) {
		int tmp = 0;
		boolean isFound = false;
		Deque<int[]> k = new LinkedList<>();
		for(int y : archers) {
			boolean[][] visited = new boolean[n][m];
			int x = n;
			isFound = false;
			Deque<int[]> q = new LinkedList<>();
			
			
			q.add(new int[] {x,y,0});
			while (!q.isEmpty()) {
				int[] archer = q.pollFirst();
				int xx = archer[0];
				int yy = archer[1];
				int dist = archer[2];
				if(isFound) break;
				
				for(int i = 0 ; i < 3 ; i ++) {
					int nx = xx + dx[i];
					int ny = yy + dy[i];
					if(nx>= 0 && nx< n && ny >= 0 && ny< m && !visited[nx][ny] && dist < d) {
						visited[nx][ny] = true;
						q.add(new int[] {nx,ny,dist+1});
						if(map[nx][ny] == 1) {
							k.add(new int[] {nx,ny});
							isFound = true;
							break;
						}
					}
					
				}
			}	
			
		}	
		
		while(!k.isEmpty()) {
			int[] ToBeKilled = k.pollFirst();
			int kx = ToBeKilled[0];
			int ky = ToBeKilled[1];
			
			if(map[kx][ky] == 1) {
				map[kx][ky] = 0;
				tmp += 1;
			}
		}
		
		return tmp;
	}

	static int getDist(int x1, int y1, int x2, int y2) {
		return Math.abs(x1-x2) + Math.abs(y1-y2); 
	}
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int ans = 0;
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		d = Integer.parseInt(st.nextToken());
		map = new int[n][m];
		map_copy = new int[n][m];
		for(int i = 0 ; i < n ; i ++) {
			st = new StringTokenizer(br.readLine());
			for(int j = 0 ; j < m ; j ++) {
				map[i][j] = Integer.parseInt(st.nextToken());
				map_copy[i][j] = map[i][j];
			}
		}
		
		
		for(int a = 0 ; a < m-2 ; a ++) {
			for(int b = a+1 ; b < m-1 ; b ++) {
				for(int c = b+1 ; c < m ; c ++) {
					int[] archer = new int[] {a,b,c};
					init();
					int cnt = 0;
					for (int i = 0 ; i < n ; i ++) {
						cnt += attack(archer);
						move();

					}
					ans = Math.max(ans, cnt);
					
				}
			}
		}
		System.out.println(ans);		
	}

}