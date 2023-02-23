# 2887. 행성 터널  2023-02-23


def find(n):
    if uf[n] == n: return n

    uf[n] = find(uf[n])
    return uf[n]


def union(A, B):
    if A < B: uf[B] = A
    else: uf[A] = B


N = int(input())
x, y, z = [], [], []
for i in range(N):
    a, b, c = map(int, input().split())
    x.append((a, i))
    y.append((b, i))
    z.append((c, i))
x.sort()
y.sort()
z.sort()

edges = []
for i in range(N - 1):
    edges.append((x[i + 1][0] - x[i][0], x[i][1], x[i + 1][1]))
    edges.append((y[i + 1][0] - y[i][0], y[i][1], y[i + 1][1]))
    edges.append((z[i + 1][0] - z[i][0], z[i][1], z[i + 1][1]))
edges.sort()

uf = [i for i in range(N)]
ans = 0
for i in range(len(edges)):
    d, a, b = edges[i]

    A, B = find(a), find(b)
    if A != B:
        union(A, B)
        ans += d

print(ans)