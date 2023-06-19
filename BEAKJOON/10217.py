# 10217. KCM Travel  2023-04-05


import sys
from collections import deque
input = sys.stdin.readline


def update_query(i, j, v):
    j += 1
    while j < M + 2:
        dp[i][j] = min(dp[i][j], v)
        j += j & -j


def get_query(i, j):
    j += 1
    temp = INF
    while 0 < j:
        temp = min(temp, dp[i][j])
        j &= j - 1
    return temp


int(input())
V, M, E = map(int, input().split())

adj_list = [[] for _ in range(V)]
for _ in range(E):
    u, v, c, t = map(int, input().split())
    if v == 1: continue
    adj_list[u - 1].append((v - 1, c, t))

INF = 10000001
dp = [[INF] * (M + 2) for _ in range(V)]

q = deque()
q.append((0, 0, 0))
update_query(0, 0, 0)
while q:
    t, i, c = q.popleft()
    if get_query(i, c) < t: continue

    for j, nc, nt in adj_list[i]:
        new_c = c + nc
        new_t = t + nt
        if new_c > M: continue

        if get_query(j, new_c) > new_t:
            update_query(j, new_c, new_t)
            q.append((new_t, j, new_c))

ans = get_query(V - 1, M)
if ans == INF:
    print("Poor KCM")
else:
    print(ans)