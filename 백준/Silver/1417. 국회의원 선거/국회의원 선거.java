import java.io.*;
import java.util.*;
public class Main {
	static int n,m;
	
	public static void main(String[] args) throws IOException{
		Scanner sc = new Scanner(System.in);
		n = sc.nextInt();
		int[] can = new int[n];
		int ans = 0;
		for (int i = 0 ; i < n ; i ++) {
			can[i] = sc.nextInt();
		}
		while(true) {
			int max = can[0];
			int idx = 0;
			for(int i = 0 ; i < n ; i++) {
				if (max <= can[i]) {
					max = can[i];
					idx = i;
				}
			}
			
			if (idx == 0) break;
			can[idx] -=1;
			can[0] += 1;
			ans += 1;
		}
		
		System.out.println(ans);
		
	}
}