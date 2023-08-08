import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Deque;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class Main {
	static int n;
	static int m;
	
	static void rotate(int[][] arr) {
		int cnt = Math.min(n, m) / 2;
		
		for(int c = 0 ; c < cnt ; c ++) {
			int tmp = arr[c][c]; 
			for(int i = c ; i < m-c-1 ; i ++) {
				arr[c][i] = arr[c][i+1];
			}
			// 오른
			for(int i = c ; i <n-c-1; i ++) {
				arr[i][m-c-1] = arr[i+1][m-c-1];
			}		
			//아래
			for(int i = m-c-1 ; i > c ; i --) {
				arr[n-c-1][i] = arr[n-c-1][i-1];
			}
			//왼쪽
			for(int i = n-c-1 ; i > c ; i --) {
				arr[i][c] = arr[i-1][c];
			}
				
			arr[c+1][c] = tmp;
			
		}



		
		
				
	}
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		int r = Integer.parseInt(st.nextToken());
		int[][] arr = new int[n][m];
		for (int i = 0 ; i < n ; i ++ ) {
			st = new StringTokenizer(br.readLine());
			for(int j = 0 ; j < m ; j ++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		for(int i = 0 ; i < r ; i ++) {
			rotate(arr);
		}
		for(int i = 0 ; i < n ; i ++) {
			for(int j = 0 ; j < m ; j ++) {
				System.out.print(arr[i][j] +" ");
			}
			System.out.println();	
		}

	}

}