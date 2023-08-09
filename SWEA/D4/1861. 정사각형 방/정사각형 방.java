import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.Scanner;

public class Solution {
	static int[][] delta = {{1,0},{0,1},{-1,0},{0,-1}};
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for(int test_case = 1 ; test_case <=T ; test_case++) {
			int n = sc.nextInt();
			int[][] room = new int[n][n];
			for(int i = 0 ; i < n ; i ++) {
				for(int j = 0 ; j < n ; j ++) {
					room[i][j] = sc.nextInt();
				}
			}
			int roomNum = 0;
			int ans = 0;
			for(int i = 0 ; i < n ; i ++) {
				for(int j = 0 ; j < n ; j ++) {
					Queue<Integer> q = new LinkedList<>();
					Queue<Integer> q2 = new LinkedList<>();
					int tmp = 1;
					int num = n*i + j;
					q.offer(num);
					q2.offer(tmp);
					
					while (!q.isEmpty()) {
						num = q.poll();
						tmp = q2.poll();
						int x = num / n;
						int y = num % n;
						
						for(int k = 0 ; k < 4 ; k ++) {
							int nx = x + delta[k][0];
							int ny = y + delta[k][1];
							if(nx>= 0 && nx < n && ny >= 0 && ny < n && (room[nx][ny] == room[x][y] + 1)) {
								q.offer(nx*n + ny);
								q2.offer(tmp+1);
							}
						}
					}

					if (ans < tmp) {
						ans = tmp;
						roomNum = room[i][j];
					}
					else if (ans == tmp) {
						roomNum = Math.min(roomNum, room[i][j]);
					}
				}
			}
			
			
			System.out.println("#"+test_case + " " + roomNum + " " + ans);
		}
	}

}