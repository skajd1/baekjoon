import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	
	public static void main(String[] args) throws IOException {
//		Scanner sc = new Scanner(System.in);
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		String[] s = br.readLine().split(" ");
		int N = Integer.parseInt(s[0]);
		int M = Integer.parseInt(s[1]);
		int[][] num = new int[N][N];
		
		for(int i = 0 ; i < N ; i ++) {
			st = new StringTokenizer(br.readLine());
			for(int j = 0 ; j < N ; j ++) {
				num[i][j] =  Integer.parseInt(st.nextToken());
			}
		}
		int[][] sum = new int[N+1][N+1];
		for(int i = 0 ; i < N ; i ++) {
			for(int j = 0 ; j < N ; j ++) {
				sum[i+1][j+1] = num[i][j] += sum[i+1][j];
			}
				
			
		}
		for(int i = 2; i < N+1 ; i ++){
			for (int j = 1 ; j < N+1; j ++) {
				sum[i][j] += sum[i-1][j];
			}
		}
		
		
		for(int i = 0 ; i < M ; i ++) {
			st = new StringTokenizer(br.readLine());
			int s_c = Integer.parseInt(st.nextToken());
			int s_r = Integer.parseInt(st.nextToken());
			int e_c = Integer.parseInt(st.nextToken());
			int e_r = Integer.parseInt(st.nextToken());

			System.out.println(sum[e_c][e_r] - sum[s_c-1][e_r] - sum[e_c][s_r-1] + sum[s_c-1][s_r-1]);
			
		}
		

	}

}
