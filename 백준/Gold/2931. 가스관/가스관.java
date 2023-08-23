import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	
	static int[] dx = {1,0,-1,0};
	static int[] dy = {0,1,0,-1};
	static int dir = 0; // 방향 변수 하 우 상 좌 0 1 2 3
	static char[][] map;
	static int r;
	static int c;
	
	static int[] move( int x, int y) { // 현재 블록에 따른 다음 위치 반환하는 함수
		int[] next = new int[2]; // 다음 위치 저장 변수 
		if(map[x][y] == '-' || map[x][y] == '|' || map[x][y] == '+') { // - 블록이나 | 블록은 방향 유지, 이동만
			next[0] = x + dx[dir];
			next[1] = y + dy[dir];
		}
		else if (map[x][y] == '1') { // 1,2,3,4번 블록은 방향 전환 필요. 방향 바꾸고 그 방향으로 이동
			if(dir == 2) dir = 1;		// 현재 방향이 2일경우 1로 
			else if(dir == 3) dir = 0; // 현재 방향이 3일경우 0으로
			next[0] = x + dx[dir];
			next[1] = y + dy[dir];
		}
		else if (map[x][y] == '2') {
			if(dir == 0) dir = 1;		//현재 방향이 0일경우 1로
			else if(dir == 3) dir = 2;  // 현재 방향이 3일경우 2로
			next[0] = x + dx[dir];
			next[1] = y + dy[dir];
		}
		else if (map[x][y] == '3') {
			if(dir == 1) dir = 2;	 // 현재 방향이 1일경우 2로
			else if(dir == 0) dir = 3; // 현재 0일경우 3으로
			next[0] = x + dx[dir];
			next[1] = y + dy[dir];
		}
		else if (map[x][y] == '4') {
			if(dir == 1) dir = 0;	// 현재 1일경우 0으로	
			else if(dir == 2) dir = 3; // 현재 2일경우 3으로
			next[0] = x + dx[dir];
			next[1] = y + dy[dir];
		}
		return next;
		
	}
	
	static char check(int x, int y) { // x,y 기준 사방 탐색해서 지워진 블록이 무엇인지 알아내는 함수
		int[][] delta = {{-1,0},{1,0},{0,-1},{0,1}}; // 상 하 좌 우 0 1 2 3
		boolean[] check = new boolean[4]; // 상 하 좌 우 어디랑 이어져있는지 체크하는 변수
		for(int i = 0 ; i < 4 ; i++) {
			int nx = x + delta[i][0];
			int ny = y + delta[i][1];
			if(0<=nx && nx < r && 0<= ny && ny< c && map[nx][ny] != '.') { // 빈칸이 아니면 해당 방향 check
				if (i == 0 ) {
					check[i] = map[nx][ny] == '|' || map[nx][ny] == '+' || map[nx][ny] == '1' || map[nx][ny] == '4';
				}
				else if(i==1) {
					check[i] = map[nx][ny] == '|' || map[nx][ny] == '+' || map[nx][ny] == '2' || map[nx][ny] == '3';
				}
				else if(i==2) {
					check[i] = map[nx][ny] == '-' || map[nx][ny] == '+' || map[nx][ny] == '1' || map[nx][ny] == '2';
				}
				else {
					check[i] = map[nx][ny] == '-' || map[nx][ny] == '+' || map[nx][ny] == '3' || map[nx][ny] == '4';
				}
			}
		}
		if(check[0]) { // 위랑 연결 -> | + 2 3 중에 하나
			if(check[2]) { // 왼쪽 연결 
				if(check[3]) { // 오른쪽 연결
					return '+';
				}
				return '3';
			}
			if(check[1]) { // 아래 연결
				return '|';
			}
			return '2';
		}
		else { // - 1 4 중에 하나
			if(check[1]) { // 아래 연결
				if(check[2]) { // 왼쪽연결
					return '4';
				}
				return '1';
			}
			return '-';	
		}
	}
	public static void main(String[] args) throws IOException {
		// |   -   +  1        2 	   3	  4
		// 세로 가로 사방 (오른 아래) (오른 위) (왼 위 ) (왼 아래)
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		r = Integer.parseInt(st.nextToken()); // r행
		c =Integer.parseInt(st.nextToken()); // c열
		map = new char[r][c]; // 지도 정보 저장 변수
		int ans[] = new int[2]; // 정답 위치 저장 변수
		char block; // 정답 블록 저장 변수
		for(int i = 0 ; i < r ; i ++) {
			map[i] = br.readLine().toCharArray(); // 지도 정보 입력 받기
		}	

		// M부터 시작해서 사방 탐색으로 경로 찾기
		// M에 인접한 블록이 가리키는 다음 칸이 빈칸이라면
		// 그 빈칸으로부터 나머지 세 방향 탐색해서 어디로 이어져있는지 확인 후에 블록 판별하기
		
		int[] now = new int[2]; // 빈칸이 아닌 블록 찾으면 저장할 변수
		for(int i = 0 ; i < r ; i ++) {
			for(int j = 0 ; j < c ; j ++) {
				if(map[i][j] == 'M') { // 출발지점 부터 탐색
					for(int k = 0 ; k < 4 ; k ++) {
						int nx = i + dx[k];
						int ny = j + dy[k];
						if (0<=nx && nx < r && 0<=ny && ny<c && map[nx][ny] !='.') { // 범위 안에 있으면서 빈칸이 아니면
							dir = k; // 시작 방향
							now[0] = nx; // 시작 블록 x 위치
							now[1] = ny; // 시작 블록 y 위치
							
							break;
						}
					
					}
					break;
				}
			}
		}
		while(true) { // 지워진 블록 위치 찾는 파트
			int[] tmp = move(now[0],now[1]);
			int x = tmp[0];
			int y = tmp[1];
			if (map[x][y] == '.') { // 지워진 블록 발견하면
				ans[0] = x; // 정답 위치에 저장
				ans[1] = y;
				break;
			}
			now[0] = x; // 못찾았으면 현재 위치 업데이트
			now[1] = y;
		}
		
		// 지워진 블록 위치 기준 사방 탐색 실시
		block = check(ans[0],ans[1]);
		System.out.println((ans[0]+1) + " " + (ans[1]+1) + " " + block); //결과 출력
	}
	

}