// No.39 광고 시간 정하기  2023-02-11


import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {

    public static void main(String[] args) throws Exception {

        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int T = Integer.parseInt(in.readLine());
        for (int tc = 1; tc <= T; tc++) {
            int L = Integer.parseInt(in.readLine());
            int N = Integer.parseInt(in.readLine());
            int[][] ads = new int[N][3];
            int arr = 0;
            for (int i = 0; i < N; i++) {
                st = new StringTokenizer(in.readLine());
                ads[i][0] = Integer.parseInt(st.nextToken());
                ads[i][1] = Integer.parseInt(st.nextToken());
                arr += ads[i][1] - ads[i][0];
                ads[i][2] = arr;
            }

            int ans = 0;
            for (int[] now: ads) {
                int end = now[0] + L;
                int endIdx = bs(end, ads);
                int time = ads[endIdx][2] - now[2] + now[1] - now[0];
                if (ads[endIdx][1] > end) time -= ads[endIdx][1] - end;

                ans = Math.max(ans, time);
            }
            System.out.println("#" + tc + " " + ans);
        }
    }

    public static int bs(int end, int[][] ads) {
        int l = 0, r = ads.length - 1;

        while (l < r) {
            int m = (l + r + 1) / 2;
            if (ads[m][0] <= end) l = m;
            else r = m - 1;
        }

        return l;
    }
}
