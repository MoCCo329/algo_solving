# 11779. 최소비용 구하기 2  2023-02-20


import heapq


N = int(input())
M = int(input())
adj_list = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    adj_list[a].append((b, c))

A, B = map(int, input().split())
INF = 1000000000
dist = [INF] * (N + 1)
vis = [False] * (N + 1)
path = [0] * (N + 1)

pq = []
heapq.heappush(pq, (0, A))
dist[A] = 0

for _ in range(N):
    d, city = heapq.heappop(pq)
    if dist[city] != d: continue
    if city == B: break

    vis[city] = True

    for next_city, dis in adj_list[city]:
        if vis[next_city]: continue
        new_dist = d + dis
        if dist[next_city] > new_dist:
            path[next_city] = city
            dist[next_city] = new_dist
            heapq.heappush(pq, (new_dist, next_city))

ans_path = [B]
while True:
    if ans_path[-1] == A: break
    ans_path.append(path[ans_path[-1]])

print(dist[B])
print(len(ans_path))
print(*ans_path[::-1])