import java.util.*;
public class Main {
	static int[] visited1;
	static int[] visited2;
	static int n,m,v;
	
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        n = scanner.nextInt();
        m = scanner.nextInt();
        v = scanner.nextInt();

        Map<Integer, List<Integer>> edge = new HashMap<>();
        visited1 = new int[n + 1];
        visited2 = new int[n + 1];
        List<int[]> tmp = new ArrayList<>();

        for (int i = 0; i < m; i++) {
            int s = scanner.nextInt();
            int e = scanner.nextInt();
            tmp.add(new int[]{s, e});
        }

        for (int i = 1; i <= n; i++) {
            edge.put(i, new ArrayList<>());
        }

        for (int[] pair : tmp) {
            int s = pair[0];
            int e = pair[1];
            edge.get(s).add(e);
            edge.get(e).add(s);
        }

        for (int i = 1; i <= n; i++) {
            Collections.sort(edge.get(i));
        }

        // BFS
        List<Integer> order1 = new ArrayList<>();
        Queue<Integer> queue = new LinkedList<>();
        queue.add(v);
        visited1[v] = 1;
        while (!queue.isEmpty()) {
            int node = queue.poll();
            order1.add(node);
            for (int x : edge.get(node)) {
                if (visited1[x] == 0) {
                    visited1[x] = 1;
                    queue.add(x);
                }
            }
        }

        // DFS
        List<Integer> order2 = new ArrayList<>();
        dfs(v, edge, order2);

        for (int num : order2) {
            System.out.print(num + " ");
        }
        System.out.println();

        for (int num : order1) {
            System.out.print(num + " ");
        }
    }

    private static void dfs(int v, Map<Integer, List<Integer>> edge, List<Integer> order2) {
        if (visited2[v] == 0) {
            visited2[v] = 1;
            order2.add(v);
            for (int x : edge.get(v)) {
                dfs(x, edge, order2);
            }
        }
    }
}