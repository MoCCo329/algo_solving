// No.25 중간값 구하기  2023-01-31


import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Collections;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Solution {

    public static void main(String[] args) throws Exception {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int T = Integer.parseInt(in.readLine());
        for (int tc = 1; tc <= T; tc++) {
            st = new StringTokenizer(in.readLine());
            int N = Integer.parseInt(st.nextToken());
            int mid = Integer.parseInt(st.nextToken());
            long ans = 0;

            PriorityQueue<Integer> lowPq = new PriorityQueue<>(Collections.reverseOrder());
            PriorityQueue<Integer> highPq = new PriorityQueue<>();
            for (int i = 0; i < N; i++) {
                st = new StringTokenizer(in.readLine());
                int a = Integer.parseInt(st.nextToken());
                int b = Integer.parseInt(st.nextToken());
                if (b > a) {
                    int temp = b;
                    b = a;
                    a = temp;
                }

                if (mid < b) {
                    lowPq.add(mid);
                    highPq.add(b);
                    highPq.add(a);
                    mid = highPq.poll();
                } else if (mid > a) {
                    highPq.add(mid);
                    lowPq.add(b);
                    lowPq.add(a);
                    mid = lowPq.poll();
                } else {
                    highPq.add(a);
                    lowPq.add(b);
                }
                ans = (ans + mid) % 20171109;
            }

            System.out.println("#" + tc + " " + ans);
        }
    }
}
