// No.37 촛불 이벤트  2023-02-12


import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Solution {

    public static void main(String[] args) throws Exception {

        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(in.readLine());
        for (int tc = 1; tc <= T; tc++) {
            long N = Long.parseLong(in.readLine());

            long l = 1, r = 1L << 31;
            long ans = -1;
            while (l <= r) {
                long m = (l + r) / 2;
                long temp = m * (m + 1) / 2;
                if (temp == N) {
                    ans = m;
                    break;
                } else if (temp < N) l = m + 1;
                else r = m - 1;
            }

            System.out.println("#" + tc + " " + ans);
        }
    }
}
