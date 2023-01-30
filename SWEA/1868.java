// No.14 파핑파핑 지뢰찾기  2023-01-30


import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Solution {

    public static void main(String[] args) throws Exception {

        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(in.readLine());
        for (int tc = 1; tc <= T; tc++) {
            int ans = 0;
            int N = Integer.parseInt(in.readLine());
            char[][] maps = new char[N][N];

            for (int i = 0; i < N; i++) {
                String line = in.readLine();
                for (int j = 0; j < N; j++) maps[i][j] = line.charAt(j);
            }

            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    if (maps[i][j] == '*') continue;

                    int cnt = 0;
                    for (int d = 0; d < 8; d++) {
                        int di = new int[] {0, 1, 1, 1, 0, -1, -1, -1}[d];
                        int dj = new int[] {1, 1, 0, -1, -1, -1, 0, 1}[d];
                        if (0 <= i + di && i + di < N && 0 <= j + dj && j + dj < N && maps[i + di][j + dj] == '*') cnt++;
                    }
                    maps[i][j] = (char) ('0' + cnt);
                }
            }

            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    if (maps[i][j] != '0') continue;

                    ans += 1;
                    maps[i][j] = '#';
                    Queue<Integer[]> q = new LinkedList<>();
                    q.add(new Integer[] {i, j});

                    while (!q.isEmpty()) {
                        Integer[] next = q.poll();
                        int ii = next[0];
                        int jj = next[1];

                        for (int d = 0; d < 8; d++) {
                            int di = new int[] {0, 1, 1, 1, 0, -1, -1, -1}[d];
                            int dj = new int[] {1, 1, 0, -1, -1, -1, 0, 1}[d];
                            if (0 <= ii + di && ii + di < N && 0 <= jj + dj && jj + dj < N) {
                                if (maps[ii + di][jj + dj] == '#' || maps[ii + di][jj + dj] == '*') continue;
                                else if (maps[ii + di][jj + dj] == '0') q.add(new Integer[] {ii + di, jj + dj});
                                maps[ii + di][jj + dj] = '#';
                            }
                        }
                    }
                }
            }

            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    if ('0' < maps[i][j] && maps[i][j] < '9') ans += 1;
                }
            }

            System.out.println("#" + tc + " " + ans);
        }
    }
}
