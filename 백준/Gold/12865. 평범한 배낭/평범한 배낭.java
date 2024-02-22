import java.util.*;
import java.io.*;

public class Main {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        int[][] wv = new int[n+1][2];
        int[][] dp = new int[k+1][n+1];
        for(int i = 1 ; i <= n ; i ++){
            st = new StringTokenizer(br.readLine());
            wv[i][0] = Integer.parseInt(st.nextToken());
            wv[i][1] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(wv, (a,b) -> a[0] - b[0]);
        for(int i = 1 ; i <= k ; i ++){
            for(int j = 1 ; j <= n ; j ++){
                int weight = wv[j][0];
                int value = wv[j][1];
                if(i >= weight){
                    dp[i][j] = Math.max(dp[i-weight][j-1] + value,dp[i][j-1]);
                }
                else dp[i][j] = dp[i][j-1];
            }
        }
        System.out.println(dp[k][n]);
    }

}