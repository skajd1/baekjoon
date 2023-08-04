import java.util.Deque;
import java.util.LinkedList;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		Deque<Integer> deque = new LinkedList<>();
		int n = sc.nextInt();
		for(int i = 0 ; i < n; i ++) {
			deque.add(i+1);
			
		}

		while(deque.size()> 1) {
			deque.pollFirst();
			deque.add(deque.pollFirst());
			
		}
		System.out.println(deque.poll());
			
	}

}