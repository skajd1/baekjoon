import java.util.Scanner;
import java.util.Stack;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt(); // 총 분 입력
		int ans = 0; // 답 초기화
		Stack<int[]> s = new Stack<>(); // 점수 계산할 스택 선언
		for(int i = 0 ; i < n ; i ++) {
			int info = sc.nextInt(); // 1인지 0인지 저장하는 변수
			int score;
			int time;
			if(info == 1) { // 해당 시점에 업무가 있으면 그 업무의 score과 time 받고 처리
				score = sc.nextInt();
				time = sc.nextInt();
				s.add(new int[] {score,time}); // 스택의 0번 인덱스에 점수, 1번인덱스에 남은 시간 저장	
			}
			if(!s.isEmpty()) { // 스택에 뭔가 있으면
				s.peek()[1] -= 1; // 시간 1만큼 감소 
				if (s.peek()[1] == 0) ans += s.pop()[0]; // 업무 제외
			}
		}
		System.out.println(ans); // 결과 출력
	}
}