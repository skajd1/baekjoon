import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class Main {
	static int l;
	static int c;
	static char[] s;
	static char[] aeiou = {'a','e','i','o','u'};
	static LinkedList<String> ans = new LinkedList<>();
	static void f(int x) {
		int a = 0;
		int b = 0;
		if(ans.size() == l) {
			for(String asdf : ans) {
				boolean check = false;
				for (char ahdma : aeiou) {
					if (asdf.charAt(0) == ahdma) {
						check = true;
						break;
					}
				}
				if(check) b+=1;
				else a+=1;
				
			}
			if(!(a>=2 && b>=1)) return;
			for(String asdf : ans) {
				System.out.print(asdf);
			}
			System.out.println();
			return;
		}
		for(int i = x ; i < c ; i ++) {
			ans.add(Character.toString(s[i]));
			f(i+1);
			ans.pollLast();
		}
	}
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		l = Integer.parseInt(st.nextToken());
		c = Integer.parseInt(st.nextToken());
		st = new StringTokenizer(br.readLine());
		s = new char[c];
		for(int i = 0 ; i < c ; i ++) {
			s[i] = st.nextToken().charAt(0);
		}
		Arrays.sort(s);
		f(0);
	}
}