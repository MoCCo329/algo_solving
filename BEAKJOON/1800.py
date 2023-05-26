# 1800. 인터넷 설치  2023-05-26


import sys
input = sys.stdin.readline


def dfs(i, k, cost):
    global ans

    if i == N:
        ans = min(ans, cost)
        return

    if cost >= ans:
        return

    for j, c in adj_list[i]:
        if k > 0 and cost < c and memo[j][k - 1] > cost:
            for temp in range(k):
                memo[j][temp] = min(memo[j][temp], cost)
            dfs(j, k - 1, cost)
        new_c = max(cost, c)
        if memo[j][k] > new_c:
            for temp in range(k + 1):
                memo[j][temp] = min(memo[j][temp], new_c)
            dfs(j, k, new_c)


N, P, K = map(int, input().split())
adj_list = [[] for _ in range(N + 1)]
for _ in range(P):
    a, b, c = map(int, input().split())
    adj_list[a].append((b, c))
    adj_list[b].append((a, c))

INF = 1000000001
ans = INF
memo = [[INF] * (K + 1) for _ in range(N + 1)]

dfs(1, K, 0)
if ans == INF:
    print(-1)
else:
    print(ans)