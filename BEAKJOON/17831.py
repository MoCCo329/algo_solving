# 17831. 대기업 승범이네  2023-06-03


import sys
sys.setrecursionlimit(200000)
input = sys.stdin.readline


def dfs(i):  # status 0 이면 맨토
    tot = 0
    max_v = 0
    max_idx = 0

    for j in c[i]:
        dfs(j)

        tot += max(dp[j])
        temp = s[i] * s[j] - max(dp[j]) + dp[j][1]
        if temp > max_v:
            max_v = temp
            max_idx = j

    dp[i][0] = tot + s[i] * s[max_idx] - max(dp[max_idx]) + dp[max_idx][1]
    dp[i][1] = tot


N = int(input())
p = [0, 1, *map(int, input().split())]
c = [[] for _ in range(N + 1)]
s = [0, *map(int, input().split())]
for i in range(2, N + 1): c[p[i]].append(i)

dp = [[0, 0] for _ in range(N + 1)]
dfs(1)

print(max(dp[1]))