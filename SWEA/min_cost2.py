def bfs(si, sj):
    q = [(si, sj)]
    while q:
        i, j = q.pop(0)
        for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N:
                temp = v[i][j] + 1 + max(arr[ni][nj] - arr[i][j], 0)
                if v[ni][nj] == 0 or v[ni][nj] > temp:
                    v[ni][nj] = temp
                    q.append([ni, nj])


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    v = [[0] * N for _ in range(N)]

    bfs(0, 0)
    print(f'#{tc} {v[N - 1][N - 1]}')