# 5719. 거의 최단 경로  2023-05-22


import sys, heapq
from collections import deque
input = sys.stdin.readline


INF = 1000000

while True:
    N, M = map(int, input().split())
    if N == 0 and M == 0: break
    S, D = map(int, input().split())
    adj_mat = [[0] * N for _ in range(N)]
    dist = [INF] * N
    vis = [0] * N
    path_vis = [[0] * N for _ in range(N)]

    for _ in range(M):
        a, b, w = map(int, input().split())
        adj_mat[a][b] = w

    pq = [(0, S)]
    dist[S] = 0
    while pq:
        d, i = heapq.heappop(pq)
        if dist[i] != d: continue
        vis[i] = 1

        if i == D: break

        for j in range(N):
            if adj_mat[i][j] == 0: continue
            if vis[j] == 1: continue
            new_d = d + adj_mat[i][j]
            if new_d < dist[j]:
                dist[j] = new_d
                heapq.heappush(pq, (new_d, j))

    vis = [0] * N
    q = deque()
    q.append(D)
    while q:
        i = q.popleft()

        for j in range(N):
            if adj_mat[j][i] == 0: continue
            if path_vis[j][i] == 1: continue
            if dist[j] + adj_mat[j][i] != dist[i]: continue

            path_vis[j][i] = 1
            q.append(j)

    dist = [INF] * N
    pq = [(0, S)]
    dist[S] = 0
    while pq:
        d, i = heapq.heappop(pq)
        if dist[i] != d: continue
        vis[i] = 1

        if i == D: break

        for j in range(N):
            if adj_mat[i][j] == 0: continue
            if vis[j] == 1 or path_vis[i][j] == 1: continue
            new_d = d + adj_mat[i][j]
            if new_d < dist[j]:
                dist[j] = new_d
                heapq.heappush(pq, (new_d, j))

    if dist[D] == INF:
        print(-1)
    else:
        print(dist[D])