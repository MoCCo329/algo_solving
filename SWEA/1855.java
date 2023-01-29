// No.15 영준이의 진짜 BFS  2023-01-29


import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Solution {

    public static void main(String[] args) throws Exception {

        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(in.readLine());
        for (int tc = 1; tc <= T; tc++) {
            int N = Integer.parseInt(in.readLine());
            LinkedList<Integer>[] adjList = new LinkedList[N];
            for (int i = 0; i < N; i++) adjList[i] = new LinkedList<>();
            int[][] parents = new int[N][17];
            int[] level = new int[N];

            StringTokenizer st = new StringTokenizer(in.readLine());
            for (int i = 1; i < N; i++) {
                int p = Integer.parseInt(st.nextToken()) - 1;
                parents[i][0] = p;
                adjList[p].add(i);
                level[i] = level[p] + 1;
            }
            getParent(N, parents);

            long ans = 0;
            int now = 0;
            Queue<Integer> q = new LinkedList<>();
            q.add(0);
            while (!q.isEmpty()) {
                int next = q.poll();
                ans += getDist(now, next, level, parents);
                now = next;
                for (int i: adjList[next]) q.add(i);
            }

            System.out.println("#" + tc + " " + ans);
        }
    }

    public static void getParent(int N, int[][] parents) {
        for (int j = 1; j < 17; j++) for (int i = 0; i < N; i++) parents[i][j] = parents[parents[i][j - 1]][j - 1];
    }

    public static int getDist(int i, int j, int[] level, int[][] parents) {
        if (level[i] > level[j]) {
            int temp = i;
            i = j;
            j = temp;
        }

        int ans = 0;
        for (int k = 16; k >= 0; k--) {
            if (level[j] - level[i] >= (1 << k)) {
                j = parents[j][k];
                ans += 1 << k;
            }
        }

        if (i == j) return ans;
        for (int k = 16; k >= 0; k--) {
            if (parents[i][k] != parents[j][k]) {
                i = parents[i][k];
                j = parents[j][k];
                ans += 2 * (1 << k);
            }
        }
        return ans + 2;
    }
}