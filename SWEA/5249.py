# 5249. 최소 신장 트리 2022-04-04

T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    adjM = [[0] * (V + 1) for _ in range(V + 1)]
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        adjM[n1][n2] = w
        adjM[n2][n1] = w

    MST = [1] + [0] * V

    s = 0
    for _ in range(V):
        u = 0
        minV = 11
        for i in range(V + 1):
            if MST[i] == 1:
                for j in range(V + 1):
                    if 0 < adjM[i][j] < minV and MST[j] == 0:
                        u = j
                        minV = adjM[i][j]
        s += minV
        MST[u] = 1

    print(f'#{tc} {s}')