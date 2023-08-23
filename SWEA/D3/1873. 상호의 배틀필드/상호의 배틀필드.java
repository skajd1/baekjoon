import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Solution {
	static int h;
	static int w;
	static char[][] map;
	static int x;
	static int y;
	static int dir;
	static HashMap<String,Integer> dirmap = new HashMap<>();
	
	static int[][] delta = {{-1,0},{0,1},{1,0},{0,-1}};
	static void shoooot() {
		int nx = x;
		int ny = y;
		while(true) {
			nx += delta[dir][0];
			ny += delta[dir][1];
			if(0<=nx && nx < h && 0<=ny && ny < w) {
				if(map[nx][ny] == '#') return;
				else if(map[nx][ny] == '*') {
					map[nx][ny] = '.';
					return;
				}
				
			}
			else return;
		}
	}
	static void changeDir(char nowDir) {
		dir = dirmap.get(Character.toString(nowDir));
		
	}
	static void move(char nowDir) {
		changeDir(nowDir);
		int nx = x + delta[dir][0];
		int ny = y + delta[dir][1];
		if(0<=nx && nx < h && 0<=ny && ny < w) {
			if(map[nx][ny] == '.') {
				x = nx;
				y = ny;
				return;
			}
		}
		
	}
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		dirmap.put("U",0);
		dirmap.put("R",1);
		dirmap.put("D",2);
		dirmap.put("L",3);
		
		int T = Integer.parseInt(br.readLine());
		for(int tc = 1; tc <= T ; tc++) {
			st = new StringTokenizer(br.readLine());
			StringBuilder sb = new StringBuilder();
			h = Integer.parseInt(st.nextToken());
			w = Integer.parseInt(st.nextToken());
			map = new char[h][w];
			for(int i = 0 ; i < h ; i ++) {
				map[i] = br.readLine().toCharArray();
			}
			int n = Integer.parseInt(br.readLine());
			char[] op = new char[n];
			op = br.readLine().toCharArray();
			
			
			for(int i = 0 ; i < h ; i ++) {
				for(int j = 0 ; j < w ; j ++) {
					if (map[i][j] == '<') {
						map[i][j] = '.';
						x = i; y = j;
						dir = 3;
					}
					else if (map[i][j] == '>') {
						map[i][j] = '.';
						x = i; y = j;
						dir = 1;
					}
					else if (map[i][j] == '^') {
						map[i][j] = '.';
						x = i; y = j;
						dir = 0;
					}
					else if (map[i][j] == 'v') {
						map[i][j] = '.';
						x = i; y = j;
						dir = 2;
					}
				}
			}
			
			for(char x : op) {
				if(x!='S') move(x);
				else shoooot();
			}
			System.out.print("#"+ tc + " ");
			for(int i = 0 ; i < h ; i ++) {
				for(int j = 0 ; j < w ; j ++) {
					if(x == i && y == j) {
						if(dir == 0) System.out.print('^');
						else if (dir == 1) System.out.print('>');
						else if (dir == 2) System.out.print('v');
						else  System.out.print('<');
						
					}
					else System.out.print(map[i][j]);
				}
				System.out.println();
			}
		}
	}

}
//		***....
//		*-..#**
//		#<.****
// SURSSSSUSLSRSSSURRDSRDS