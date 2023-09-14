import java.io.*;
import java.util.*;
public class Main {
	static int n;

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		Integer[] num = new Integer[n];
		for(int i = 0 ; i < n ; i++) {
			num[i] = Integer.parseInt(br.readLine());
		}
		Arrays.sort(num,(x,y)->y-x);
		int cnt = 0;
		int ans = 0;
		for(int x : num) {
			cnt++;
			if(cnt == 3) {
				cnt = 0;
				continue;
			}
			ans+=x;
		}
		System.out.println(ans);
	}
}