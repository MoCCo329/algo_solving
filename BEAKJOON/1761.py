# 1761. 정점들의 거리  2023-02-28


from collections import deque
import heapq


def findLCA(a, b):
    if lank[a] < lank[b]:
        a, b = b, a
    aOrigin = a
    bOrigin = b

    for l in range(k - 1, -1, -1):
        if lank[a] - lank[b] >= (1 << l):
            a = parent[a][l]
    if a == b:
        return dist[aOrigin] - dist[b]

    for l in range(k - 1, -1, -1):
        if parent[a][l] != parent[b][l]:
            a = parent[a][l]
            b = parent[b][l]
    lca = parent[a][0]
    return dist[aOrigin] + dist[bOrigin] - 2 * dist[lca]


N = int(input())
k = 1
temp = 2
while temp < N:
    temp *= 2
    k += 1
adj_list = [[] for _ in range(N + 1)]
parent = [[0] * k for _ in range(N + 1)]
lank = [0] * (N + 1)

for _ in range(N - 1):
    a, b, d = map(int, input().split())
    adj_list[a].append((b, d))
    adj_list[b].append((a, d))

q = deque()
q.append((1, 0))
parent[1][0] = 1
while q:
    now = q.popleft()
    for nex, d in adj_list[now[0]]:
        if lank[nex] != 0 or nex == 1: continue
        q.append((nex, now[1] + 1))
        lank[nex] = now[1] + 1
        parent[nex][0] = now[0]

for l in range(1, k):
    for i in range(1, N + 1):
        parent[i][l] = parent[parent[i][l - 1]][l - 1]

INF = 100000000
dist = [INF] * (N + 1)
dist[1] = 0
q = [(0, 1)]
while q:
    now = heapq.heappop(q)
    if dist[now[1]] != now[0]: continue

    for next_node, next_d in adj_list[now[1]]:
        new_dist = now[0] + next_d
        if dist[next_node] > new_dist:
            if dist[next_node] == INF:
                heapq.heappush(q, (new_dist, next_node))
            dist[next_node] = new_dist

M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    print(findLCA(a, b))