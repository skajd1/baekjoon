import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int n,d,k,c;
		n = Integer.parseInt(st.nextToken());
		d = Integer.parseInt(st.nextToken());
		k = Integer.parseInt(st.nextToken());
		c = Integer.parseInt(st.nextToken());
		int[] sushi = new int[n];
		for(int i = 0 ; i < n ; i ++) {
			sushi[i] = Integer.parseInt(br.readLine());
		}
		int ans = 1;
        int[] visited = new int[d+1];
        visited[c] = 1;
        int cnt = 1;
        for(int i = 0 ; i < k ; i ++){
            if(visited[sushi[i]] == 0) cnt+=1;
            visited[sushi[i]] += 1;
        }
		for(int i = k ; i < n+k ; i ++) {
            visited[sushi[i-k]] -= 1;
            if(visited[sushi[i-k]] == 0) cnt -= 1;
            if(visited[sushi[i%n]] == 0) cnt += 1;
            visited[sushi[i%n]] += 1;
            ans = Math.max(ans, cnt);
            if(ans == k+1) break;
		}
		System.out.println(ans);
	}
}