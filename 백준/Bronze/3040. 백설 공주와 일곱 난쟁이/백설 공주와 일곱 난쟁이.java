import java.util.Scanner;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[] a = new int[9];
        //List<Integer> a = new ArrayList<>();
        
        for (int i = 0; i < 9; i++) {
            a[i] = scanner.nextInt();
        }
        
        for (int mask = 0; mask < (1 << 9); mask++) {
            List<Integer> subset = new ArrayList<>();
            for (int i = 0; i < 9; i++) {
                if ((mask & (1 << i)) != 0) {
                    subset.add(a[i]);
                }
            }
            
            if (subset.size() == 7) {
                int sum = 0;
                for (int num : subset) {
                    sum += num;
                }
                
                if (sum == 100) {
                    for (int num : subset) {
                        System.out.println(num);
                    }
                    break;
                }
            }
        }
    }
}