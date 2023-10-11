import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
	static long p = 1234567891;
	static long pow(long a , long b) {
		if(b == 0) return 1;
		long tmp = pow(a, b/2);
		long res = tmp*tmp % p;
		if(b%2 == 0) return res;
		
		return (res*a) % p;
	}
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int T = Integer.parseInt(st.nextToken());
		long[] f = new long[1000001];
		f[1] = 1;
		for(int i = 2; i <= 1000000; i ++) {
			f[i] = (i * f[i-1])%p ;
		}
		for(int t = 1 ; t <= T ; t ++) {
			long ans = 0;
			st = new StringTokenizer(br.readLine());
			int n = Integer.parseInt(st.nextToken());
			int r = Integer.parseInt(st.nextToken());
			long tmp1 = f[n];
			long tmp2 = f[n-r];
			long tmp3 = f[r];
			ans = (tmp1 * pow((tmp2 * tmp3)%p, p-2)%p ) % p;
			System.out.println("#" + t + " " + ans);
			
		}
	}
}