import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	static int[] dx = {0,0,1,-1};
	static int[] dy = {1,-1,0,0};
	static int ans = 1;
	static int r;
	static int c;
	static char[][] board;
	static boolean[] visited = new boolean[26];
	static void dfs(int cnt,int x, int y) {
        ans = Math.max(ans, cnt);

        for(int i = 0 ; i < 4 ; i ++){
            int nx = x + dx[i];
            int ny = y + dy[i];
					
            if(0<= nx && nx <r && 0<= ny && ny < c && visited[(int)board[nx][ny] - 'A'] == false){
							
                visited[(int)board[nx][ny] - 'A'] = true;
                dfs(cnt+1,nx,ny);
                visited[(int)board[nx][ny] - 'A'] = false;
            }
        }	
	}
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] input = br.readLine().split(" ");
		r = Integer.parseInt(input[0]);
		c = Integer.parseInt(input[1]);
		board = new char[r][c];
		for(int i = 0 ; i < r ; i ++) {
			board[i] = br.readLine().toCharArray();
		}
		visited[(int)board[0][0]-'A'] = true;
		dfs(1,0,0);
		System.out.println(ans);
	}
}

