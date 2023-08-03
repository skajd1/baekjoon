import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc  = new Scanner(System.in);
		int lenDNA = sc.nextInt();
		int lenSubSet = sc.nextInt();
		String DNA = sc.next();
		int A = sc.nextInt();
		int C = sc.nextInt();
		int G = sc.nextInt();
		int T = sc.nextInt();
		int ans = 0;
		int AA = 0;
		int CC = 0;
		int GG = 0;
		int TT = 0;
		String s =DNA.substring(0,lenSubSet);
		for(int i = 0 ; i < lenSubSet; i ++) {
			if (s.charAt(i) == 'A') {
				AA+=1;
			}
			else if (s.charAt(i) == 'C') {
				CC+=1;
			}
			else if (s.charAt(i) == 'G') {
				GG+=1;
			}
			else if (s.charAt(i) == 'T') TT+=1;
		}
		if(AA >= A && CC >= C && GG >= G && TT >= T) {
			ans += 1;
		}
		for(int i = 0 ; i < lenDNA-lenSubSet; i ++) {
			if (DNA.charAt(i) == 'A') {
				AA-=1;
			}
			else if (DNA.charAt(i) == 'C') {
				CC-=1;
			}
			else if (DNA.charAt(i) == 'G') {
				GG-=1;
			}
			else if (DNA.charAt(i) == 'T') TT-=1;
			if (DNA.charAt(i+lenSubSet) == 'A') {
				AA+=1;
			}
			else if (DNA.charAt(i+lenSubSet) == 'C') {
				CC+=1;
			}
			else if (DNA.charAt(i+lenSubSet) == 'G') {
				GG+=1;
			}
			else if (DNA.charAt(i+lenSubSet) == 'T') TT+=1;
			if(AA >= A && CC >= C && GG >= G && TT >= T) {
				ans += 1;
			}
			
		}
		System.out.println(ans);
		
		
	}

}