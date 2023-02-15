// No.35 Inversion Counting  2023-02-15


import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {

    public static void main(String[] args) throws Exception {

        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int T = Integer.parseInt(in.readLine());
        for (int tc = 1; tc <= T; tc++) {
            int N = Integer.parseInt(in.readLine());
            int k = 1;
            while (k < N) k <<= 1;
            int[] arr = new int[N];
            int[] sTree = new int[k << 1];
            st = new StringTokenizer(in.readLine());
            for (int i = 0; i < N; i++) arr[i] = Integer.parseInt(st.nextToken()) - 1;

            long ans = 0;
            for (int i = 0; i < N; i++) {
                int start = k, end = k + arr[i] - 1;
                int tempAns = 0;
                while (start <= end) {
                    if ((start & 1) == 1) tempAns += sTree[start++];
                    if ((end & 1) == 0) tempAns += sTree[end--];
                    start >>= 1;
                    end >>= 1;
                }
                ans += arr[i] - tempAns;

                sTree[k + arr[i]] = 1;
                int idx = (k + arr[i]) / 2;
                while (idx > 0) {
                    sTree[idx] = sTree[idx * 2] + sTree[idx * 2 + 1];
                    idx >>= 1;
                }
            }

            System.out.println("#" + tc + " " + ans);
        }
    }
}
