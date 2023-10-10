import java.io.*;
import java.util.*;

public class Solution {
	
	static int[] rotateMagnet(int dir, int[] mag) {
		int[] newMag = new int[8];
		if (dir == 1) {
			for(int i = 0 ; i < 8 ; i ++) {
				newMag[(i+1)%8] = mag[i];
			}
		}
		else {
			for(int i = 1 ; i < 8 ; i ++) {
				newMag[i-1] = mag[i];
			}
			newMag[7] = mag[0];
		}
		return newMag;
	}
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int T = Integer.parseInt(st.nextToken());
		for(int t = 1; t <= T ; t ++) {
			int ans = 0;
			st = new StringTokenizer(br.readLine());
			int k = Integer.parseInt(st.nextToken());
			int[][] magnet = new int[4][8];
			for(int i = 0 ; i < 4 ; i ++) {
				st = new StringTokenizer(br.readLine());
				for(int j = 0 ; j < 8 ; j ++) {
					magnet[i][j] = Integer.parseInt(st.nextToken());
				}
			}
			int[][] rotate = new int[k][2];
			for(int i = 0 ; i < k ; i++) {
				st = new StringTokenizer(br.readLine());
				rotate[i] = new int[] {Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken())};
			}
			int[][] direction = {{1,-1,1,-1},{-1,1,-1,1}};
			for(int[] r : rotate) {
				boolean[] tmp = new boolean[4];
				int num = r[0];
				int dir = r[1];
				int dnum;
				if (dir == 1) {
					if (num == 2 || num == 4) dnum = 1;
					else dnum = 0;
				}
				else {
					if(num==1 || num == 3) dnum = 1;
					else dnum = 0;
				}
				tmp[num-1] = true;
				
				if (num == 1) {
					if (magnet[0][2] != magnet[1][6]) {
						tmp[1] = true;
						if(magnet[1][2] != magnet[2][6]) {
							tmp[2] = true;
							if(magnet[2][2] != magnet[3][6])
								tmp[3] = true;
						}
					}
				}
				else if(num == 4) {
					if(magnet[3][6] != magnet[2][2]) {
						tmp[2] =  true;
						if(magnet[2][6] != magnet[1][2]) {
							tmp[1] = true;
							if(magnet[1][6] != magnet[0][2])
								tmp[0] = true;
						}
					}
					
				}
				else if(num == 2){
					if(magnet[0][2] != magnet[1][6]) tmp[0] = true;
					if(magnet[2][6] != magnet[1][2]) {
						tmp[2] = true;
						if(magnet[2][2] != magnet[3][6]) tmp[3] = true;
					}
				}
				else {
					if(magnet[3][6] != magnet[2][2]) tmp[3] = true;
					if(magnet[2][6] != magnet[1][2]) {
						tmp[1] = true;
						if(magnet[1][6] != magnet[0][2]) tmp[0] = true;
					}
					
				}
				for(int i = 0 ; i < 4 ; i ++) {
					if (tmp[i]) {
						magnet[i] = rotateMagnet(direction[dnum][i], magnet[i]);
					}
				}
			}
			int[] score = {1,2,4,8};
			for(int i = 0 ; i < 4 ; i ++) {
				if(magnet[i][0] == 1) ans += score[i];
			}
			System.out.println("#" + t + " " + ans);
		}
	}
}