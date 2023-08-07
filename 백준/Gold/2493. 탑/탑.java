import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		int[] arr = new int[n];
		StringTokenizer st = new StringTokenizer(br.readLine());
		for(int i = 0 ; i < n ; i ++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		Stack<Integer> s = new Stack<>();
		int[] result = new int[n];
		
		for (int i = 0 ; i < n ; i ++) {
			while (s.size() > 0) {
				if(arr[i] > arr[s.peek()]) {
					s.pop();
				}
				else 
					break;
			}
			if (s.isEmpty() == false) {
				result[i] = s.peek() + 1;
				
			}
			s.add(i);
		}
		for(int i = 0 ; i < n ; i ++) {
			System.out.print(result[i] +" ");
		}
	}

}