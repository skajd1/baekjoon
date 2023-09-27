import java.awt.Point;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.StringTokenizer;

public class Main {
	static int n;
	static boolean[] visited;
	static Point sg, fest, conv[];
	static StringBuilder sb = new StringBuilder();
	
	
	static void bfs() {
		ArrayDeque<Point> q = new ArrayDeque<>(); 
		visited = new boolean[n];
		q.add(sg);
		while(!q.isEmpty()) {
			Point now = q.pollFirst();
			if(Math.abs(now.x -fest.x) + Math.abs(now.y - fest.y)<=1000) {
				sb.append("happy\n");
				return;
			}
			int idx = 0;
			for (Point c : conv) {
				if(Math.abs(c.x - now.x) + Math.abs(c.y - now.y)<=1000 && !visited[idx]) {
					visited[idx] = true;
					q.addLast(c);
				}
				idx += 1;
			}
		}
		sb.append("sad\n");
	}
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int T = Integer.parseInt(br.readLine());
		for(int t = 1 ; t <= T ; t ++) {
			n = Integer.parseInt(br.readLine());
			
			StringTokenizer st = new StringTokenizer(br.readLine());
			sg = new Point();
			sg.x = Integer.parseInt(st.nextToken());
			sg.y = Integer.parseInt(st.nextToken());
			
			conv = new Point[n];
			for(int i = 0 ; i < n ; i++) {
				st = new StringTokenizer(br.readLine());
				conv[i] = new Point();
				conv[i].x = Integer.parseInt(st.nextToken());
				conv[i].y = Integer.parseInt(st.nextToken());
			}
			
			st = new StringTokenizer(br.readLine());
			fest = new Point();
			fest.x = Integer.parseInt(st.nextToken());
			fest.y = Integer.parseInt(st.nextToken());
			
			bfs();
		}
		System.out.println(sb.toString());
	}
}