# 1865 웜홀.  2022-09-10


import sys
INF = sys.maxsize


def bellman_ford(i):
    D = [INF] * (N + 1)
    D[i] = 0

    for cnt in range(N + 1):

        for j in range(1, N + 1):
            for k in range(1, N + 1):
                if adj_arr[j][k] == INF: continue

                if D[k] > D[j] + adj_arr[j][k]:
                    D[k] = D[j] + adj_arr[j][k]
                    if cnt == N:
                        return True

    return False


for tc in range(int(input())):
    N, M, W = map(int, input().split())  # 지점 수, 도로 수, 웜홀 수
    adj_arr = [[INF] * (N + 1) for _ in range(N + 1)]

    for _ in range(M):
        a, b, w = map(int, input().split())
        adj_arr[a][b] = min(adj_arr[a][b], w)
        adj_arr[b][a] = min(adj_arr[a][b], w)
    for _ in range(W):
        a, b, w = map(int, input().split())
        adj_arr[a][b] = min(adj_arr[a][b], -w)

    if bellman_ford(1):
        print('YES')
    else:
        print('NO')