import java.io.*;
import java.util.*;
public class Main {
    // q에 indegree가 0인 인덱스들 넣고 
    // q에서 poll하면서 각 ans[인덱스] += time[인덱스] 하기.
    // poll할 때 그 인덱스를 자식으로 갖고 있는 애들 indegree -=1 해주고 만약 0이면 q에 넣기
    static int n;
    static LinkedList<Integer>[] graph;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        int[] indegree = new int[n+1];
        int[] times = new int[n+1];
        int[] ans = new int[n+1];
        graph = new LinkedList[n+1];
        for(int i = 0 ; i < n ; i++) {
            graph[i+1] = new LinkedList<Integer>();
        }
        for(int i = 0 ; i < n ; i++) {
            st = new StringTokenizer(br.readLine());
            times[i+1] = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            while(b != -1) {
                indegree[i+1] += 1;
                graph[b].add(i+1);
                b =Integer.parseInt(st.nextToken());
            }
        }
        LinkedList<Integer> q = new LinkedList<>();
        for(int i = 1 ; i <= n ; i++) {
            if (indegree[i] == 0) q.add(i);
        }
        for(int i = 1; i <= n ; i++){
            ans[i] = times[i];

        }
        while(!q.isEmpty()) {
            int node = q.poll();
            while(!graph[node].isEmpty()) {
                int x = graph[node].poll();
                indegree[x] -= 1;

                ans[x] = Math.max(times[x] + ans[node], ans[x]);
                if(indegree[x] == 0) q.add(x);
            }
        }
        for(int i = 1; i <= n ; i++) System.out.println(ans[i]);
    }
}