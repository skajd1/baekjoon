import java.util.*;
import java.io.*;
public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int n = Integer.parseInt(br.readLine());
        PriorityQueue<Integer> pq1 = new PriorityQueue<>((o1, o2) -> o2-o1);
        PriorityQueue<Integer> pq2 = new PriorityQueue<>();

        pq1.add(Integer.parseInt(br.readLine()));
        sb.append(pq1.peek());

        for(int i = 0 ; i < n-1 ; i ++){
            int num = Integer.parseInt(br.readLine());
            if(pq1.peek() < num) pq2.add(num);
            else pq1.add(num);

            if(pq1.size() > pq2.size() +1 ) pq2.add(pq1.poll());
            else if(pq2.size() > pq1.size()) pq1.add(pq2.poll());

            sb.append("\n").append(pq1.peek());

        }
        System.out.println(sb.toString());

    }
}