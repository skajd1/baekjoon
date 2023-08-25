import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        int node_num = Integer.parseInt(input[0]);
        int edge_num = Integer.parseInt(input[1]);
        int nodeStart = Integer.parseInt(br.readLine());

        ArrayList<ArrayList<Node>> graph = new ArrayList<>();
        for (int i = 0; i <= node_num; i++) {
            graph.add(new ArrayList<>());
        }

        for (int i = 0; i < edge_num; i++) {
            input = br.readLine().split(" ");
            int u = Integer.parseInt(input[0]);
            int v = Integer.parseInt(input[1]);
            int w = Integer.parseInt(input[2]);
            graph.get(u).add(new Node(v, w));
        }

        int[] distance = new int[node_num + 1];
        Arrays.fill(distance, Integer.MAX_VALUE);
        distance[nodeStart] = 0;

        PriorityQueue<Node> pq = new PriorityQueue<>((a, b) -> Integer.compare(a.distance, b.distance));
        pq.offer(new Node(nodeStart, 0));

        while (!pq.isEmpty()) {
            Node current = pq.poll();
            int current_node = current.node;
            int current_dist = current.distance;

            if (current_dist > distance[current_node]) continue;

            for (Node neighbor : graph.get(current_node)) {
                int v = neighbor.node;
                int w = neighbor.distance;
                if (distance[v] > current_dist + w) {
                    distance[v] = current_dist + w;
                    pq.offer(new Node(v, distance[v]));
                }
            }
        }

        for (int i = 1; i <= node_num; i++) {
            if (distance[i] == Integer.MAX_VALUE) {
                System.out.println("INF");
            } else {
                System.out.println(distance[i]);
            }
        }
    }

    static class Node {
        int node;
        int distance;

        public Node(int node, int distance) {
            this.node = node;
            this.distance = distance;
        }
    }
}