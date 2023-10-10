import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
	static int r,c,t,board[][];
	

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		r = Integer.parseInt(st.nextToken());
		c = Integer.parseInt(st.nextToken());
		t = Integer.parseInt(st.nextToken());
		board = new int[r][c];
		for(int i = 0 ; i < r ; i++) {
			st = new StringTokenizer(br.readLine());
			for(int j = 0 ; j < c ; j ++) {
				board[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		int now = 0;
		int ans = 0;
		ArrayList<int[]> air_tmp;
		ArrayList<int[]> cleaner;
		int[] dx = {1,-1,0,0};
		int[] dy = {0,0,1,-1};
		while (now != t) {
			now += 1;
			air_tmp = new ArrayList<>();
			cleaner = new ArrayList<>();
			for(int i = 0 ; i < r ;  i++) {
				for(int j = 0 ; j < c ; j++) {
					if(board[i][j] == -1) {
						cleaner.add(new int[] {i,j});
						continue;
					}
					if(board[i][j] >= 5 ) {
						int tmp = board[i][j];
						for(int k = 0 ; k < 4 ; k++) {
							int nx = i + dx[k];
							int ny = j + dy[k];
							if(0<= nx && nx < r && 0<= ny && ny < c && board[nx][ny] != -1) {
								air_tmp.add(new int[] {(tmp/5), nx, ny});
								board[i][j] = board[i][j] - (tmp / 5);
							}
						}
					}
				}
			}
			for(int[] tmp : air_tmp) {
				board[tmp[1]][tmp[2]] += tmp[0];
			}
			
			for(int i = cleaner.get(0)[0] -1; i > 0 ; i --) {
				board[i][0] = board[i-1][0];
			}
			for(int i = cleaner.get(1)[0] + 1; i < r-1 ; i++) {
				board[i][0] = board[i+1][0];
			}
			for(int i = 0 ; i < c-1 ; i++) {
				board[0][i] = board[0][i+1];
				board[r-1][i] = board[r-1][i+1];
			}
			for(int i = 0 ; i < cleaner.get(0)[0]; i ++) {
				board[i][c-1] = board[i+1][c-1];
			}
			for(int i = r-1 ; i > cleaner.get(1)[0]; i --) {
				board[i][c-1] = board[i-1][c-1];
			}
			for(int i = c-1 ; i > 0 ; i--) {
				board[cleaner.get(0)[0]][i] = board[cleaner.get(0)[0]][i-1];
				board[cleaner.get(1)[0]][i] = board[cleaner.get(1)[0]][i-1];
			}
			board[cleaner.get(0)[0]][1] = 0;
			board[cleaner.get(1)[0]][1] = 0;
		}
		for(int i = 0 ; i < r ; i ++) {
			for(int j = 0 ; j < c ; j++) {
				ans += board[i][j];
			}
		}
		System.out.println(ans+2);
	}
}