# 1647. 도시 분할 계획  2022-07-21


import heapq
N, M = map(int, input().split())
q = []
for _ in range(M):
    a, b, w = map(int, input().split())
    heapq.heappush(q, (w, a, b))

uf = [i for i in range(N + 1)]


def find(x):
    if uf[x] == x:
        return x
    uf[x] = find(uf[x])
    return uf[x]


def union(x, y):
    X, Y = find(x), find(y)
    if X > Y:
        uf[X] = Y
    else:
        uf[Y] = X


mst = []
ans = 0
while q:
    w, a, b = heapq.heappop(q)
    if find(a) != find(b):
        mst.append(w)
        union(a, b)
        ans += w
        temp = w

print(ans - temp)