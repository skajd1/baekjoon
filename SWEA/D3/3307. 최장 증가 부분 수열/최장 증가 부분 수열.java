import java.util.Arrays;
import java.util.Scanner;

public class Solution {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for(int t = 1 ; t <= T ; t++) {
			int N = sc.nextInt();
			int[] arr = new int[N];
			int[] LIS = new int[N];
			
			for(int i = 0 ; i < N ; i++) {
				arr[i] = sc.nextInt();
			}
			int end = 0;
			for(int i = 0 ; i < N ; i ++) {
				int insPosition = Arrays.binarySearch(LIS,0,end,arr[i]);
				insPosition = Math.abs(insPosition) - 1;
				LIS[insPosition] = arr[i];
				if(end == insPosition) end +=1;
			}
			System.out.println("#" + t + " " + end);
			
		}
	}

}