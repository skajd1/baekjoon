import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.StringTokenizer;

public class Solution {
	
	static int n,k;
	static char[] num;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int T = Integer.parseInt(st.nextToken());
		for(int t = 1; t <= T ; t ++) {
			int ans = 0;
			st = new StringTokenizer(br.readLine());
			n = Integer.parseInt(st.nextToken());
			k = Integer.parseInt(st.nextToken());
			num = new char[n];
			num = br.readLine().toCharArray();
			HashSet<String> set = new HashSet<>();
			for(int i = 0 ; i < n/4 ; i ++) {
				StringBuilder sb = new StringBuilder();
				for(int j = 0 ; j < n ; j++) {
					sb.append(num[(i+j)%n]);
					if(j % (n/4) == n/4 - 1) {
						set.add(sb.toString());
						sb = new StringBuilder();
					}
				}
			}
			ArrayList<Integer> list = new ArrayList<>();
			for(String s : set) {
				list.add(Integer.parseInt(s,16));
			}
			list.sort((n1,n2) -> n2-n1);

			System.out.println("#" + t + " " + list.get(k-1));
		}
	}

}