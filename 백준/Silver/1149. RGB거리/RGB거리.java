import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int n = Integer.parseInt(br.readLine());
        int[][] RGB = new int[n][3];
        for(int i = 0 ; i < n ; i ++){
            st = new StringTokenizer(br.readLine());
            for(int j = 0 ; j < 3 ; j ++)
                RGB[i][j] = Integer.parseInt(st.nextToken());
        }
        for(int i = 1 ; i < n ; i++){
            RGB[i][0] += Math.min(RGB[i-1][1], RGB[i-1][2]);
            RGB[i][1] += Math.min(RGB[i-1][0], RGB[i-1][2]);
            RGB[i][2] += Math.min(RGB[i-1][0], RGB[i-1][1]);
        }
        System.out.println(Math.min(Math.min(RGB[n-1][0], RGB[n-1][1]), RGB[n-1][2]));
    }    
}