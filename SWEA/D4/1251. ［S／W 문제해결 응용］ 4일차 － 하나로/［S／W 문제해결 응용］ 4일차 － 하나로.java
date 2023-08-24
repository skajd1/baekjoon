import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;
import java.util.StringTokenizer;

public class Solution {
	static int n;
	static int[] x;
	static int[] y;
	static double E;
	static int[] parents;
	
	static int find(int a){
		if(parents[a] == a) return a;
		return parents[a] = find(parents[a]);
	
	}
	static boolean union(int a, int b){
		int rootA = find(a);
		int rootB = find(b);
		if (rootA == rootB) return false;
		parents[rootB] = rootA;
		return true;
	}
	static double getDist(int x1, int y1, int x2, int y2) {
		double dx =Math.abs(x1-x2);
		double dy =Math.abs(y1-y2);
		
		return dx*dx + dy*dy;
	}
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int t = Integer.parseInt(br.readLine());
		for(int tc = 1; tc <=t ; tc ++) {
			n = Integer.parseInt(br.readLine());
			x = new int[n];
			y = new int[n];
			parents = new int[n+1];
		    st = new StringTokenizer(br.readLine());
			for(int i = 0 ; i < n ; i++) {
				x[i] = Integer.parseInt(st.nextToken());
				parents[i+1] = i+1;
			}
			st = new StringTokenizer(br.readLine());
			for(int i = 0 ; i < n ; i++) {
				y[i] = Integer.parseInt(st.nextToken());
			}
			E = Double.parseDouble(br.readLine());
			double ans = 0;
			
			List<double[]> list = new ArrayList<>();
			
			for(int i = 0 ; i < n ; i ++) {
				for(int j = i ; j < n ; j ++) {
					if(i==j) continue;
					 list.add(new double[] {i,j,getDist(x[i],y[i],x[j],y[j])});
				}
			}
			Collections.sort(list,new Comparator<double[]>() {

				@Override
				public int compare(double[] o1, double[] o2) {
					return (int) (o1[2] - o2[2]);
				}
			});
			for(int i = 0 ; i < list.size(); i ++) {
				double[] tmp = list.get(i);
				if(union((int)tmp[0],(int)tmp[1])) ans += tmp[2];
			}
			System.out.println("#" + tc + " " + Math.round(ans * E));
		}
	}
}