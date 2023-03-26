# 1810. 징검다리 달리기2  2023-03-26


import heapq, sys
input = sys.stdin.readline


V, end = map(int, input().split())
nodes = [(0, 0)]
exist_nodes = dict()
for i in range(1, V + 1):
    x, y = map(int, input().split())
    nodes.append((x, y))
    exist_nodes[(x, y)] = i

INF = 80000000000
dist = [INF] * (V + 1)
vis = [False] * (V + 1)

dist[0] = 0
hq = [(0, 0)]

while hq:
    d, i = heapq.heappop(hq)
    if dist[i] != d: continue

    vis[i] = True
    if nodes[i][1] >= end:
        print(round(d))
        exit(0)

    x1, y1 = nodes[i]
    for di in range(-2, 3):
        for dj in range(-2, 3):
            x2, y2 = x1 + di, y1 + dj
            j = exist_nodes.get((x2, y2), 0)
            if j == 0: continue
            if vis[j]: continue

            new_dist = d + (di ** 2 + dj ** 2) ** 0.5
            if new_dist < dist[j]:
                dist[j] = new_dist
                heapq.heappush(hq, (new_dist, j))

print(-1)