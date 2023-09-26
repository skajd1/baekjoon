import java.util.Scanner;

public class Main {
	static int[][] board = new int[9][9];
	
	static boolean[] getNum(int x, int y) {
		boolean[] candidate = new boolean[10];
		// x,y가 속한 3*3 크기 확인
		int nx = (x/3) * 3;
		int ny = (y/3) * 3;
		for(int i = nx; i < nx + 3; i++) {
			for(int j = ny; j < ny + 3; j++) {
				candidate[board[i][j]] = true;
			}
		}
		// x 행, y 열 확인
		for(int i = 0 ; i < 9; i ++) {
			candidate[board[x][i]] = true;
			candidate[board[i][y]] = true;
		}
		return candidate;
	}
	static void dfs(int x, int y) {
		if(x == 9) {
			for(int i = 0 ; i < 9 ; i++) {
				for(int j = 0 ; j < 9 ; j++) {
					System.out.print(board[i][j]);
				}
				System.out.println();
			}
			System.exit(0);
		}
		if(y == 9) {
			dfs(x+1,0);
			return;
		}
		if(board[x][y] == 0) {
			boolean[] candidate = getNum(x,y);
			for(int i = 1 ; i < 10 ; i++) {
				if(!candidate[i]) {
					board[x][y] = i;
					dfs(x,y+1);
					board[x][y] = 0;
				}
			}
		}
		else dfs(x,y+1);
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		for(int i = 0 ; i < 9 ; i++) {
			String tmp = sc.next();
			for(int j = 0 ; j < 9 ; j++) {
				board[i][j] = (int)(tmp.charAt(j) - '0');
			}
		}
		dfs(0,0);
	}

}