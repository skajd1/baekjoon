import java.awt.Point;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int T = Integer.parseInt(st.nextToken());
		for(int t = 1; t <= T ; t ++) {
			int ans = -1;
			st = new StringTokenizer(br.readLine());
			int n = Integer.parseInt(st.nextToken());
			int dist = -1;
			boolean flag = true;
			for(int i = 0 ; i < n ; i ++) {
				st = new StringTokenizer(br.readLine());
				int x = Integer.parseInt(st.nextToken());
				int y = Integer.parseInt(st.nextToken());
				if ((Math.abs(x) + Math.abs(y)) % 2 != dist%2 && dist != -1) {
					flag = false;
				}
				dist = Math.max(dist,Math.abs(x) + Math.abs(y));
			}
			int cnt = 0;
			if(flag) {
				int sum = 0;
				while(true) {
					sum += cnt;
					if(sum >= dist && (sum-dist) % 2 == 0) break;
					cnt += 1;
				}
				ans = cnt;
			}

			System.out.println("#" + t + " " + ans);
		}
	}

}