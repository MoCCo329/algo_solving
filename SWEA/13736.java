// No.34 사탕 분배  2023-02-15


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
            int A = Integer.parseInt(st.nextToken());
            int B = Integer.parseInt(st.nextToken());
            int C = A + B;
            int K = Integer.parseInt(st.nextToken());

            long m = pow(K, C);
            long ans = m * Math.min(A, B) % C;
            ans = Math.min(ans, C - ans);

            System.out.println("#" + tc + " " + ans);
        }
    }

    public static int pow(int k, int mod) {
        if (k == 0) return 1;
        if (k == 1) return 2;
        long temp = pow(k / 2, mod);
        if (k % 2 == 1) return (int) (temp * temp * 2 % mod);
        else return (int) (temp * temp % mod);
    }
}