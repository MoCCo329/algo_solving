# 1795. 인수의 생일 파티 2022-04-06

def dijkstra(X, N):
    U = [0] * (N + 1)
    U[X] = 1
    D = [100000] * (N + 1)
    for i in range(1, N + 1):
        D[i] = adjM[X][i]
    D[X] = 0

    for _ in range(N - 1):
        minV = 100000
        j = 0
        for i in range(1, N + 1):
            if U[i] == 0 and minV > D[i]:
                minV = D[i]
                j = i
        U[j] = 1
        for k in range(1, N + 1):
            if 0 < adjM[j][k] < 101:
                D[k] = min(D[k], D[j] + adjM[j][k])

    return D

T = int(input())
for tc in range(1, T + 1):
    N, M, X = map(int, input().split())
    adjM = [[100000] * (N + 1) for _ in range(N + 1)]
    for _ in range(M):
        n1, n2, w = map(int, input().split())
        adjM[n1][n2] = w
    ans = 0

    D = dijkstra(X, N)
    adjM = list(map(list, zip(*adjM)))
    D = list(map(sum, zip(D, dijkstra(X, N))))

    print(f'#{tc} {max(D[1:])}')