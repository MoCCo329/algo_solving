# 13907. 세금  2023-03-12


import heapq


def dijkstra(s):
    dist = [1000000] * (V + 1)
    path = [0] * (V + 1)

    pq = []
    heapq.heappush(pq, (0, s, s))
    while pq:
        now = heapq.heappop(pq)
        if dist[pq[1]] != pq[0]: continue

        path[now[1]] = now[2]

        for next_node in adj_list[now[1]]:
            if path[next_node[0]]: continue
            next_dist = now[0] + next_node[1]
            if next_dist < dist[next_node[0]]:
                pq.add((next_dist, next_node[0], now[1]))

    path_count = [0] * (V + 1)
    for i in range(1, V + 1):
        while path[i] != i:
            path_count += 1
            i = path[i]

    return dist, path


V, E, K = map(int, input().split())
S, D = map(int, input().split())
adj_list = [[] * (V  + 1)]
for _ in range(E):
    a, b, d = map(int, input().split())
    adj_list[a].append((b, d))
    adj_list[b].append((a, d))

S_dist, S_path = dijkstra(S)
D_dist, D_path = dijkstra(D)

fee = 0
for k in range(K + 1):
    if k != 0:
        fee += int(input())

    min_idx = 0
    min_v = 1000000
    for i in range(1, V + 1):
        