# 10217. KCM Travel  2023-04-05


import heapq, sys
input = sys.stdin.readline


T = int(input())
for tc in range(1, T + 1):
    V, M, E = map(int, input().split())

    adj_list = [[] for _ in range(V)]
    for _ in range(E):
        u, v, c, t = map(int, input().split())
        adj_list[u - 1].append((v - 1, c, t))

    INF = 10000001
    dp = [[INF] * (M + 1) for _ in range(V)]

    hq = [(0, 0, 0)]
    for i in range(M + 1):
        dp[0][i] = 0
    while hq:
        t, i, c = heapq.heappop(hq)
        if dp[i][c] != t: continue

        for j, nc, nt in adj_list[i]:
            new_c = c + nc
            new_t = t + nt
            if new_c > M: continue

            if dp[j][new_c] > new_t:
                for k in range(new_c, M + 1):
                    if dp[j][k] <= new_t: break
                    dp[j][k] = new_t
                heapq.heappush(hq, (new_t, j, new_c))

    ans = min(dp[V - 1])
    if ans == INF:
        print("Poor KCM")
    else:
        print(ans)