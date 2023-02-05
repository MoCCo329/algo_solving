# 11657. 타임머신  2023-02-05


def df():
    D[1] = 0

    for i in range(V):
        for j in range(E):
            cur, nex, d = edges[j]
            if D[cur] != INF and D[nex] > D[cur] + d:
                D[nex] = D[cur] + d
                if i == V - 1:
                    return True
    return False


V, E = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(E)]
INF = V * 10000
D = [INF] * (V + 1)
if df():
    print(-1)
else:
    for i in range(2, V + 1):
        if D[i] == INF:
            print(-1)
        else:
            print(D[i])