import java.io.IOException;
import java.util.Scanner;
import java.util.StringTokenizer;

public class Main {
	
	public static void main(String[] args) throws IOException {
		Scanner sc = new Scanner(System.in);
//		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = (sc.nextInt());
		int M = (sc.nextInt());
		int[] num = new int[N];
		
		for(int i = 0 ; i < N ; i ++) {
			num[i] =  sc.nextInt();
		}
		int[] sum = new int[N+1];
		sum[1] = num[0];
		for(int i = 2 ; i < N+1 ; i ++) {
			sum[i] = sum[i-1] + num[i-1];
		}
		for(int i = 0 ; i < M ; i ++) {
			
			int start = sc.nextInt();
			int end = sc.nextInt();
			System.out.println(sum[end] - sum[start-1]);
		}

	}

}
