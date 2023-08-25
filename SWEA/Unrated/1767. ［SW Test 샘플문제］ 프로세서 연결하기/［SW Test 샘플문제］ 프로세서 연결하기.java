import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
	
	static int ans;
    static int core;
	static int n;
	static int[][] delta = {{1,0},{0,1},{-1,0},{0,-1}};
	static int[][] cell;
	
	static void init(int[][] cell1, int[][] cell2) {
		for(int i = 0 ; i < n; i ++) {
			for(int j = 0 ; j < n ; j++) {
				cell1[i][j] = cell2[i][j];
			}
		}
	}
    //벽에 닿으면 cnt 반환
    //전선이나 코어에 닿으면 -1 반환
	static int makeLine(int[][] nextCell, int x, int y, int dir) {
        int nx = x + delta[dir][0];
        int ny = y + delta[dir][1];
        int len = 0;
        while(nx >= 0 && nx < n && ny >= 0 && ny < n) {
            if(nextCell[nx][ny] == 0) {
                nextCell[nx][ny] = 2;
                len++;
            }
            else return -1;
            nx += delta[dir][0];
            ny += delta[dir][1];
        }
		return len;
	}
	// 코어 갯수 최대로 (now 최소 )
	static void dfs(int x, int y, int now, int length, int[][] cellNow) {
        if(y == n) {
            dfs(x+1,0,now,length,cellNow);
            return;
        }
        if(x == n) {
            if (core < now){
                core = now;
                ans = length;
            }
            else if (core == now) ans = Math.min(ans,length);
            return;
        }
		// 현재 x,y가 가장자리가 아니고 , 전선이 아니고, 코어 이면,
		// 방향 4개 포문
		// 현재 방향에 전선이나 코어가 없으면
		// 그 방향 cell 전선 연결 및 전선 갯수 세서 now에 더한 뒤 dfs 넘겨주기, cell 복사본도 넘겨주기
		if(x != 0 && x != n-1 && y != 0 && y != n-1 && cellNow[x][y] == 1) {
            int[][] cell_copy = new int[n][n];
			for(int i = 0 ; i < 4 ; i ++) {
                init(cell_copy,cellNow);
                int cnt = makeLine(cell_copy,x,y,i);
                if( cnt == -1) continue;
                dfs(x,y+1,now+1,length+cnt,cell_copy);
			}
		}
        dfs(x,y+1,now,length,cellNow);
	}
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
		int T = Integer.parseInt(br.readLine());
		for(int tc = 1; tc <= T ; tc ++) {
			ans = 0;
            core = 0;
			n = Integer.parseInt(br.readLine());
            cell = new int[n][n];
			for(int i = 0 ; i < n ; i++) {
                st = new StringTokenizer(br.readLine());
				for(int j = 0 ; j < n ; j++) {
                    cell[i][j] = Integer.parseInt(st.nextToken());
                }
			}
            dfs(0,0,0,0,cell);			
			System.out.println("#" + tc + " " + ans);
		}
	}
}