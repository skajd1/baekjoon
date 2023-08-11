import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int ans = -1;
		for(int i = 0 ; i <= 1000; i ++) {
			for(int j = 0 ; j < 1667; j ++) {
				if ( i* 5 + j * 3 == n) {
					ans = i + j;
				}
			}
		}
		System.out.println(ans);
	}

}