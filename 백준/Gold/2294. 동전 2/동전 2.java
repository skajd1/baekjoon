import java.util.*;
import java.io.*;
public class Main {

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());
    int n = Integer.parseInt(st.nextToken());
    int k = Integer.parseInt(st.nextToken());
    Set<Integer> coins = new HashSet<>();
    for(int i = 0 ; i < n ; i ++){
      coins.add(Integer.parseInt(br.readLine()));
    }
    int[] coinArr = new int[coins.size()];
    int idx = 0;
    for(int coin : coins){
      coinArr[idx++] = coin;
    }
    Arrays.sort(coinArr);
    int[][] dp = new int[k+1][coinArr.length+1];
    for(int i = 1 ; i <= k ; i ++){
      Arrays.fill(dp[i], 10001);
    }

    for(int i = 1 ; i <= k ; i ++){
      for(int j = 1 ; j <= coinArr.length ; j ++){
        int coin = coinArr[j-1];
        if(i < coin){
          dp[i][j] = dp[i][j-1];
          continue;
        }
        dp[i][j] = Math.min(dp[i][j-1], dp[i-coin][j] + 1);

      }
    }
    if (dp[k][coinArr.length] != 10001)
      System.out.println(dp[k][coinArr.length]);
    else
      System.out.println(-1);
  }

}