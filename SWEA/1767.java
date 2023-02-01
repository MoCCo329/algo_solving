// No.13 프로세서 연결하기  2023-02-01


import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Solution {

    public static int maxK = 0;
    public static int ans = 0;

    public static void main(String[] args) throws Exception {

        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(in.readLine());
        for (int tc = 1; tc <= T; tc++) {
            int N = Integer.parseInt(in.readLine());
            int[][] maps = new int[N][N];
            for (int i = 0; i < N; i++) {
                StringTokenizer st = new StringTokenizer(in.readLine());
                for (int j = 0; j < N; j++) maps[i][j] = Integer.parseInt(st.nextToken());
            }

            List<int[]> cells = new ArrayList<>();
            for (int i = 1; i < N - 1; i++) {
                for (int j = 1; j < N - 1; j++) {
                    if (maps[i][j] == 1) cells.add(new int[] {i, j});
                }
            }

            maxK = 0;
            ans = 0;
            dfs(0, 0, 0, cells, maps, N);
            System.out.println("#" + tc + " " + ans);
        }
    }

    public static void dfs(int k, int cnt, int idx, List<int[]> cells, int[][] maps, int N) {
        // 연결한 셀 수 k, 연결 길이 cnt, 이번에 진행할 셀의 idx

        if (k > maxK) {
            maxK = k;
            ans = cnt;
        }
        else if (k == maxK) ans = Math.min(ans, cnt);

        if (idx >= cells.size()) return;

        int i = cells.get(idx)[0], j = cells.get(idx)[1];
        dFor: for (int d = 0; d < 4; d++) {
            int di = new int[] {0, 1, 0, -1}[d];
            int dj = new int[] {1, 0, -1, 0}[d];
            int ni = i + di, nj = j + dj;
            int chk = 0;
            while (0 <= ni && ni < N && 0 <= nj && nj < N) {
                if (maps[ni][nj] != 0) continue dFor;
                ni += di;
                nj += dj;
                chk += 1;
            }
            if (chk > 0) {
                for (int l = 1; l <= chk; l++) {
                    maps[i + di * l][j + dj * l] = 2;
                }
                dfs(k + 1, cnt + chk, idx + 1, cells, maps, N);
                for (int l = 1; l <= chk; l++) {
                    maps[i + di * l][j + dj * l] = 0;
                }
            }
        }
        dfs(k, cnt, idx + 1, cells, maps, N);
    }
}
