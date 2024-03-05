import java.util.*;
import java.io.*;

public class Main {
  static int n;
  static boolean chkXRange(int x, int d){
    return x + d < n;
  }
  static boolean chkYRange(int y, int d){
    return y + d < n;
  }
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    n = Integer.parseInt(br.readLine());
    int[][] board = new int[n][n];
    for(int i = 0 ; i < n ; i ++){
      StringTokenizer st = new StringTokenizer(br.readLine());
      for(int j = 0 ; j < n ; j ++){
        board[i][j] = Integer.parseInt(st.nextToken());
      }
    }
    long[][] dp = new long[n][n];
    dp[0][0] = 1;
    for(int i = 0 ; i < n ; i ++){
      for(int j = 0 ; j < n ; j ++){
        if(board[i][j] == 0 ) {
          if(i == n-1 && j == n-1 ){
            System.out.println(dp[i][j]);
            return;
          }
          continue;
        }
        if(chkXRange(i, board[i][j])) dp[i+board[i][j]][j] += dp[i][j];
        if(chkYRange(j, board[i][j])) dp[i][j+board[i][j]] += dp[i][j];
      }
    }
    System.out.println(dp[n-1][n-1]);
  }
}