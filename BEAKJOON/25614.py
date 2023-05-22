# 25614. 자리 바꾸기  2023-05-22


import sys
input = sys.stdin.readline


N, M = map(int, input().split())
vis = [0] * (N + 1)
mod_memo = [-1] * (N + 1)
order = list(map(int, input().split()))
ans = [0] * N

for i in range(1, N + 1):
    if vis[i] == 1: continue

    path = []
    while vis[i] == 0:
        vis[i] = 1
        path.append(i)
        i = order[i - 1]

    L = len(path)

    if mod_memo[L] != -1:
        t = mod_memo[L]
    else:
        t = mod_memo[L] = M % L

    for j in range(L):
        ans[path[j] - 1] = path[(j + t) % L]

print(*ans, sep=' ')