# 5551. 쇼핑몰  2023-06-06


import sys
import heapq
import math
input = sys.stdin.readline


N, M, K = map(int, input().split())
adj_list = [[] for _ in range(N + 1)]
for i in range(M):
    a, b, w = map(int, input().split())
    adj_list[a].append((b, w))
    adj_list[b].append((a, w))

INF = sys.maxsize
d = [INF] * (N + 1)
vis = [False] * (N + 1)
pq = []
for _ in range(K):
    k = int(input())
    d[k] = 0
    heapq.heappush(pq, (0, k))

while pq:
    dist, i = heapq.heappop(pq)
    if d[i] != dist: continue
    vis[i] = True

    for j, w in adj_list[i]:
        new_dist = dist + w
        if vis[j] or d[j] <= new_dist: continue
        d[j] = new_dist
        heapq.heappush(pq, (new_dist, j))

ans = 0
for i in range(1, N + 1):
    for j, w in adj_list[i]:
        ans = max(ans, (d[i] + d[j] + w) / 2)

print(math.ceil(ans) if int(ans) != ans else math.floor(ans))