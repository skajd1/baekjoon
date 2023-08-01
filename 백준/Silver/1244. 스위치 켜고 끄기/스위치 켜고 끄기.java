import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

//남학생 1 여학생 2
// 남학생은 자기 번호 배수인 스위치 상태 바꾸기
// 여학생은 자기 번호 대칭으로 같은 상태인 스위치 구간이 가장 긴 구간을 전부 바꾸기

public class Main {
	static int[] swit;
	public static void change(int index) {
		swit[index] = (swit[index] == 0) ? 1 : 0;
	}
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int numSwitch = Integer.parseInt(br.readLine());
		swit = new int[numSwitch];
		StringTokenizer st = new StringTokenizer(br.readLine());
		for(int i = 0; i < numSwitch; i ++) {
			swit[i] = Integer.parseInt(st.nextToken());
		}
		int numStud = Integer.parseInt(br.readLine());
		int[][] studInfo = new int[numStud][2];
		for(int i = 0 ; i < numStud; i ++) {
			st = new StringTokenizer(br.readLine());
			studInfo[i][0] = Integer.parseInt(st.nextToken());
			studInfo[i][1] = Integer.parseInt(st.nextToken());
			
		}
		
		for (int[] info : studInfo) {
			if (info[0] == 1) {
				for(int i = 0 ; i < numSwitch; i ++) {
					if ((i+1) % info[1] == 0) {
						
						change(i);
					}
				}
			}
			else {
				int index = info[1]-1; 
				change(index);
				int tmp = 1;
				while(index + tmp < numSwitch && index - tmp >= 0) {
					if (swit[index + tmp] == swit[index-tmp]) {
						change(index+tmp);
						change(index-tmp);
					}
					else break;
					tmp += 1;
				}
			}
		}
		for(int i = 0 ; i < numSwitch; i ++){
            System.out.print(swit[i] + " ");
            if (i > 0 && (i+1) % 20 == 0) System.out.println();
            
        }
		
	}

}
