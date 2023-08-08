import java.util.Arrays;
import java.util.Scanner;

public class Solution {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for(int test_case = 1 ; test_case <= T ; test_case++) {
			int ans = -1;
			int n = sc.nextInt();
			int m = sc.nextInt();
			int[] w = new int[n];
			for(int i = 0; i < n ; i ++) {
				w[i] = sc.nextInt();
			}
			Arrays.sort(w);
			int left = 0;
			int right = w.length-1;
			while(left != right) {
				if (w[left] + w[right] == m) {
					ans = m;
					break;
				}
				else if (w[left] + w[right] < m) {
					ans = Math.max(w[left]+w[right], ans);
					left += 1;
				}
				else {
					right -= 1;
				}
			}
//			for(int i = w.length-1; i >= 1 ; i --) {
//				for(int j = i-1; j >= 0; j --) {
//					ans = w[i]+w[j] <= m ? Math.max(ans, w[i] + w[j]) : ans ;
//				}
//			}
			System.out.println("#"+test_case + " " + ans);
		}
	}

}
//1 2 3 4 5 6