// No.21 0/1 Knapsack  2023-02-02


import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.StringTokenizer;

public class Solution {

    public static void main(String[] args) throws Exception {

        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(in.readLine());
        for (int tc = 1; tc <= T; tc++) {
            StringTokenizer st = new StringTokenizer(in.readLine());
            int N = Integer.parseInt(st.nextToken());
            int K = Integer.parseInt(st.nextToken());

            int[][] items = new int[N][2];
            for (int i = 0; i < N; i++) {
                st = new StringTokenizer(in.readLine());
                for (int j = 0; j < 2; j++) items[i][j] = Integer.parseInt(st.nextToken());
            }
            Arrays.sort(items, new Comparator<int[]>() {
                @Override
                public int compare(int[] o1, int[] o2) {
                    return o1[0] - o2[0];
                }
            });
            int[] dp = new int[K + 1];

            for (int[] item: items) {
                for (int i = K; i >= item[0]; i--) {
                    dp[i] = Math.max(dp[i], dp[i - item[0]] + item[1]);
                }
            }

            System.out.println("#" + tc + " " + dp[K]);
        }
    }
}
