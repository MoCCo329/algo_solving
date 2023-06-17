# 1647. 도시 분할 계획  2022-07-21


import sys
input = sys.stdin.readline


def find(x):
    if uf[x] == x:
        return x
    uf[x] = find(uf[x])
    return uf[x]


def union(x, y):
    X, Y = find(x), find(y)
    if lank[X] > lank[Y]:
        uf[Y] = X
        lank[X] += lank[Y]
    else:
        uf[X] = Y
        lank[Y] += lank[X]


N, M = map(int, input().split())
q = [list(map(int, input().split())) for _ in range(M)]
q.sort(key=lambda x: x[2])

uf = [i for i in range(N + 1)]
lank = [1] * (N + 1)

g_cnt = N
ans = 0
for i in range(M):
    if g_cnt == 2:
        break
    a, b, w = q[i]
    if find(a) != find(b):
        union(a, b)
        ans += w
        g_cnt -= 1

print(ans)