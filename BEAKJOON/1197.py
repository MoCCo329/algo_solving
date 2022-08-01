# 1197. 최소 스패닝 트리  2022-08-01


def find(x):
    if x == uf[x]:
        return x
    uf[x] = find(uf[x])
    return uf[x]


def union(x, y):
    X = find(x)
    Y = find(y)
    if X > Y:
        uf[Y] = X
    else:
        uf[X] = Y


V, E = map(int, input().split())
adj_list = [list(map(int, input().split())) for _ in range(E)]
adj_list.sort(key=lambda x: (x[2]))

uf = [i for i in range(V + 1)]
ans = 0
for e in adj_list:
    a, b, w = e
    if find(a) != find(b):
        ans += w
        union(a, b)

print(ans)