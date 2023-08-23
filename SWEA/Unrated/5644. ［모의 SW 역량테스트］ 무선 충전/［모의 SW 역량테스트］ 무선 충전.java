import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;
// A는 0,0시작  B는 9,9 시작
// 총 10*10 크기
// 그리디하게 탐색 -> T = t 일 때 가장 큰 값만 취하면 그게 최적해
// 0 1 2 3 4
// x 상 하 좌 우
class BC{
	int x;
	int y;
	int range;
	int power;
	
	BC(int x, int y, int range, int power) {
		this.x = y-1;
		this.y = x-1;
		this.range = range;
		this.power = power;
	}
	
	boolean isInRange(int x, int y) {
		if(getDist(x,y, this.x, this.y) <= this.range) return true;	
		return false;
	}
	static int getDist(int x1, int y1, int x2, int y2) {
		return Math.abs(x1-x2) + Math.abs(y1-y2); 
	}
	
}

public class Solution {
	
	static int ans;
	static int[][] delta = {{0,0},{-1,0},{0,1},{1,0},{0,-1}};
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int t = Integer.parseInt(br.readLine());
		for(int test_case = 1; test_case <= t ; test_case++) {
			ans = 0;
			st = new StringTokenizer(br.readLine());
			int m = Integer.parseInt(st.nextToken()); //이동시간
			int a = Integer.parseInt(st.nextToken()); //BC 몇개인지
			int[][] A = new int[m+1][2];
			int[][] B = new int[m+1][2];
			B[0][0] = 9;
			B[0][1] = 9;
			
			st = new StringTokenizer(br.readLine());
			for(int i = 0 ; i < m ; i ++) {
				int dir = Integer.parseInt(st.nextToken());
				int nx = A[i][0] + delta[dir][0];
				int ny = A[i][1] + delta[dir][1];
				A[i+1][0] = nx;
				A[i+1][1] = ny;
						
			}
			st = new StringTokenizer(br.readLine());
			for(int i = 0 ; i < m ; i ++) {
				int dir = Integer.parseInt(st.nextToken());
				int nx = B[i][0] + delta[dir][0];
				int ny = B[i][1] + delta[dir][1];
				B[i+1][0] = nx;
				B[i+1][1] = ny;
				
			}			
			
			BC[] bc = new BC[a];
			for(int i = 0 ; i < a ; i ++) {
				st = new StringTokenizer(br.readLine());
				int x =Integer.parseInt(st.nextToken());
				int y = Integer.parseInt(st.nextToken());
				int range = Integer.parseInt(st.nextToken());
				int power = Integer.parseInt(st.nextToken());
				bc[i] = new BC(x,y,range,power);
			}
			
			
			for(int i = 0; i <= m ; i++) {
				int tmp = 0;
				int[] A_power = new int[a];
				int[] B_power = new int[a];
				for(int j = 0 ; j < a ; j++) {
					if(bc[j].isInRange(A[i][0], A[i][1])) A_power[j] = bc[j].power;
					if(bc[j].isInRange(B[i][0], B[i][1])) B_power[j] = bc[j].power;
				}
				if(a == 1) {
					if(A_power[0] == B_power[0]) {
						tmp = Math.max(tmp, A_power[0]);
					}
					else {
						tmp = Math.max(tmp,Math.max(A_power[0], B_power[0]));
					}
				}
				else {
					
					for(int j = 0 ; j < a; j ++) {
						for(int k = 0 ; k < a; k ++) {
							if(j == k) continue;
							tmp = Math.max(tmp, A_power[j] + B_power[k]);
						}
					}
				}
				ans += tmp;		
			}			
			System.out.println("#" + test_case + " " + ans);
		}
		
	}

}