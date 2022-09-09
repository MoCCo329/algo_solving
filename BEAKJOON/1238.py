# 1238. 파티  2022-09-09


import heapq


def dijkstra(i):
    hq = []
    heapq.heappush(hq, (0, i))
    D = [-1] * N
    D[i] = 0

    while hq:
        min_d, min_idx = heapq.heappop(hq)
        if D[min_idx] != min_d: continue

        for target_idx, target_dist in adj_list[min_idx]:
            new_dist = D[min_idx] + target_dist

            if D[target_idx] == -1 or D[target_idx] > new_dist:
                D[target_idx] = new_dist
                heapq.heappush(hq, (new_dist, target_idx))
    return D


N, M, X = map(int, input().split())
adj_list = [[] for _ in range(N)]
for _ in range(M):
    a, b, w = map(int, input().split())
    adj_list[a - 1].append((b - 1, w))

X_D = dijkstra(X - 1)
ans = 0
for i in range(N):
    if i == X - 1: continue
    temp_D = dijkstra(i)
    if ans < X_D[i] + temp_D[X - 1]:
        ans = X_D[i] + temp_D[X - 1]
print(ans)


# adj_list 에 넣을 때 a, b를 반대로 넣고 target을 시작으로 다익스트라를 돌리면 한번에 모든 점에서 타겟으로의 최소거리를 구할 수 있다.