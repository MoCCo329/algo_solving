# 1753. 최단경로  2022-09-10


import heapq


V, E = map(int, input().split())
S = int(input())

adj_list = [dict() for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    if adj_list[u].get(v, 0):
        adj_list[u][v] = min(adj_list[u][v], w)
    else:
        adj_list[u][v] = w

D = [-1] * (V + 1)
D[S] = 0
q = []
heapq.heappush(q, (0, S))

while q:
    min_d, min_idx = heapq.heappop(q)
    if D[min_idx] != min_d: continue

    for target_idx, target_d in adj_list[min_idx].items():
        if D[target_idx] == -1 or D[target_idx] > min_d + target_d:
            D[target_idx] = min_d + target_d
            heapq.heappush(q, (D[target_idx], target_idx))

for i in range(1, V + 1):
    if D[i] == -1:
        print('INF')
    else:
        print(D[i])