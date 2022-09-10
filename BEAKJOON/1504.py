# 1504 특정한 최단 경로.  2022-09-10


import heapq


def dijkstra(i):
    hq = []
    D = [-1] * N
    D[i] = 0
    heapq.heappush(hq, (0, i))

    while hq:
        min_d, min_idx = heapq.heappop(hq)
        if D[min_idx] != min_d: continue

        for j in range(N):
            if min_idx == j or adj_arr[min_idx][j] == 0: continue
            new_d = adj_arr[min_idx][j] + min_d
            if D[j] > new_d or D[j] == -1:
                D[j] = new_d
                heapq.heappush(hq, (new_d, j))

    return D


N, E = map(int, input().split())
adj_arr = [[0] * N for _ in range(N)]
for _ in range(E):
    a, b, w = map(lambda x: int(x) - 1, input().split())
    adj_arr[a][b] = w + 1
    adj_arr[b][a] = w + 1
v1, v2 = map(lambda x: int(x) - 1, input().split())

D_start = dijkstra(0)
D_end = dijkstra(N - 1)
D_v1 = dijkstra(v1)

ans = -1
if D_start[v1] + D_end[v2] <= D_start[v2] + D_end[v1] and D_start[v1] != -1 and D_end[v2] != -1:
    ans = D_start[v1] + D_end[v2]
elif D_start[v1] + D_end[v2] >= D_start[v2] + D_end[v1] and D_start[v2] != -1 and D_end[v1] != -1:
    ans = D_start[v2] + D_end[v1]

if D_v1[v2] == -1 or ans == -1:
    ans = -1
else:
    ans += D_v1[v2]

print(ans)