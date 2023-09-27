import java.awt.Point;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.StringTokenizer;
import java.io.*;
import java.util.*;

public class Main {
	static int r,c;
	static String[][] board;
	static ArrayDeque<int[]> q = new ArrayDeque<>();
	static int ans;
	static int[] dx = {0,0,1,-1};
    static int[] dy = {1,-1,0,0};
    static boolean[][] visited;
	static boolean flag;


	static boolean isInRange(int x, int y) {
		if(0<=x && x<r && 0<=y && y<c) return true;
		else return false;
	}

	static void water() {
        
		for(int i = 0 ; i < r ; i ++) {
			for(int j = 0 ; j < c ; j ++) {
                if(board[i][j].equals("*")) {
                    for(int k = 0 ; k < 4 ; k++){
                        int nx = i + dx[k];
                        int ny = j + dy[k];
						if(!isInRange(nx,ny)) continue;
                        if(board[nx][ny].equals(".") || board[nx][ny].equals("S")){
                            q.add(new int[] {nx,ny});
                        }
                    }
                }
			}
		}
        while(!q.isEmpty()) {
            int[] tmp = q.poll();
            int x = tmp[0];
            int y = tmp[1];
            board[x][y] = "*";
        }

	}

	static void go() {
		boolean canMove = false;
		for(int i = 0 ; i < r ; i++){
			for(int j = 0 ; j < c ; j++){
				
				if(board[i][j].equals("S")) {
					for(int k = 0 ; k < 4 ; k++) {
						int nx = i + dx[k];
						int ny = j + dy[k];
						if(!isInRange(nx,ny)) continue;
						
						if(board[nx][ny].equals(".")) {
							q.add(new int[] {nx,ny});
							canMove = true;
						}
						else if(board[nx][ny].equals("D")) {
							flag = true;
							System.out.println(ans);
							return;
						}
					}
				}
			}
		}
		if(!canMove) {
			flag = true;
			System.out.println("KAKTUS");
			return;
		}
		while(!q.isEmpty()) {
			int[] tmp = q.poll();
			int x = tmp[0];
			int y = tmp[1];
			board[x][y] = "S";
		}
		
	}
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		r = Integer.parseInt(st.nextToken());
		c = Integer.parseInt(st.nextToken());
        board = new String[r][c];
        visited = new boolean[r][c];
		for(int i = 0 ; i < r ; i++) {
			String tmp = br.readLine();
			for(int j = 0 ; j < c ; j ++) {
				board[i][j] = tmp.substring(j,j+1);
				if(board[i][j].equals("S")) {
                    visited[i][j] = true;
				}
			}
		}
        
        while(!flag) {
            ans += 1;
        	go();
        	water();
			
        }
        
	}
}