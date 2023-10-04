import java.util.Arrays;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc =new Scanner(System.in);
		String text = sc.nextLine(); 
		String pattern = sc.nextLine();
		int[] p = new int[pattern.length()];
		
		for(int i = 0, j = 1 ; j < pattern.length(); j++) {
			while(i > 0 && pattern.charAt(i) != pattern.charAt(j)) {
				i = p[i-1];
			}
			if (pattern.charAt(i) == pattern.charAt(j)) {
				i += 1;
				p[j] = i;
			}
		}
		int cnt = 0;
		StringBuilder sb = new StringBuilder();
		for(int i =0, j = 0; i<text.length(); i++) {
			while(j > 0 && text.charAt(i) != pattern.charAt(j)) {
				j = p[j-1];
			}
			if(text.charAt(i) == pattern.charAt(j)) {
				if(j == pattern.length() -1) {
					cnt++;
					sb.append((i+1 -pattern.length() + 1) + " ");
					j = p[j];
				}
				else {
					j++;
				}				
			}
		}
		System.out.println(cnt);
		System.out.println(sb.toString());
	}
}