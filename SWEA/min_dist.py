T = int(input())
for tc in range(1, T + 1):
    N, E = map(int, input().split())
    adjM = [[10000000] * (N + 1) for _ in range(N + 1)]
    for i in range(N + 1):
        adjM[i][i] = 0
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        adjM[n1][n2] = w

    D = [10000000] * (N + 1)
    U = [0] * (N + 1)
    for i in range(N):
        D[i] = adjM[0][i]

    for _ in range(N):
        minV = 10000000
        w = 0
        for i in range(N + 1):
            if U[i] == 0 and minV > D[i]:
                minV = D[i]
                w = i
                break
        U[w] = 1
        for n in range(N + 1):
            if 0 < adjM[w][n] < 10000000:
                D[n] = min(D[n], D[w] + adjM[w][n])

    print(f'#{tc} {D[-1]}')