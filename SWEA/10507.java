// No.36 영어 공부  2023-02-14


import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {

    public static void main(String[] args) throws Exception {

        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int T = Integer.parseInt(in.readLine());
        for (int tc = 1; tc <= T; tc++) {
            st = new StringTokenizer(in.readLine());
            int N = Integer.parseInt(st.nextToken()), P = Integer.parseInt(st.nextToken());
            boolean[] day = new boolean[1000001];
            st = new StringTokenizer(in.readLine());
            for (int i = 0; i < N; i++) day[Integer.parseInt(st.nextToken())] = true;

            int ans = 0;
            int i = 0, j = 0;
            int cnt = 0;
            while (i <= j && j < 1000001) {
                if (day[j]) j++;
                else if (cnt < P) {
                    cnt++;
                    j++;
                } else {
                    if (!day[i]) cnt--;
                    i++;
                }
                if (cnt == P) ans = Math.max(ans, j - i);
            }

            System.out.println("#" + tc + " " + ans);
        }
    }
}
