# 1267. 작업순서 2022-04-06

for tc in range(1, 11):
    V, E = map(int, input().split())
    arr = list(map(int, input().split()))
    adjM_in = [[0] * (V + 1) for _ in range(V + 1)]
    adjM_out = [[0] * (V + 1) for _ in range(V + 1)]
    for i in range(E):
        n1, n2 = arr[2 * i], arr[2 * i + 1]
        adjM_out[n1][n2] = 1
        adjM_in[n2][n1] = 1

    U = []
    visited = [0] * (V + 1)
    for _ in range(V):
        for i in range(1, V + 1):
            if visited[i] == 1:
                continue
            for j in range(1, V + 1):
                if adjM_in[i][j] == 1:
                    break
            else:
                U.append(i)
                visited[i] = 1
                for j in range(1, V + 1):
                    if adjM_out[i][j] == 1:
                        adjM_in[j][i] = 0
                break

    print(f'#{tc}', *U)