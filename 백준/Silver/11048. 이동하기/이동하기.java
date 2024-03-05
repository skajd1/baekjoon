import java.util.*;
import java.io.*;
public class Main {

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());
    int n = Integer.parseInt(st.nextToken());
    int m = Integer.parseInt(st.nextToken());
    int[][] board = new int[n][m];
    int[][] dp = new int[n+1][m+1];
    for(int i = 0 ; i < n ; i ++){
      st = new StringTokenizer(br.readLine());
      for(int j = 0 ; j < m ; j ++){
        board[i][j] = Integer.parseInt(st.nextToken());
        if(i == 0 || j == 0){
          dp[i+1][j+1] = board[i][j];
        }
      }
    }
    for(int i = 1 ; i <= n ; i ++){
      for(int j = 1 ; j <= m ; j ++){
        dp[i][j] = Math.max(dp[i][j], Math.max(dp[i-1][j], dp[i][j-1]) + board[i-1][j-1]);
      }
    }
    System.out.println(dp[n][m]);

  }
}