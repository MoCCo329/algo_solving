// No.38 사탕 가방  2023-02-13


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
            int N = Integer.parseInt(st.nextToken());
            long M = Long.parseLong(st.nextToken());
            long[] aList = new long[N];
            st = new StringTokenizer(in.readLine());
            for (int i = 0; i < N; i++) aList[i] = Long.parseLong(st.nextToken());


            long l = 0, r = (long) 1e18;
            while (l < r) {
                long m = l / 2 + r / 2 + 1;
                long tempAns = 0;
                for (int i = 0; i < N; i++) tempAns += aList[i] / m;
                if (tempAns >= M) l = m;
                else r = m - 1;
            }

            System.out.println("#" + tc + " " + l);
        }
    }
}
