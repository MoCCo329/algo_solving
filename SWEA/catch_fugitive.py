def bfs(i, j, N, M, L):
    q = []
    q.append((i, j))
    v[i][j] = 1
    while q:
        i, j = q.pop(0)
        for di, dj in t_list[arr[i][j]]:
            ni, nj = i+di, j+dj
            if 0 <= ni <N and 0 <= nj < M and ([-di, -dj] in t_list[arr[ni][nj]]) and v[ni][nj] == 0:
                q.append((ni, nj))
                v[ni][nj] = v[i][j] + 1

T = int(input())
for tc in range(1, T+1):
    N, M, i, j, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    v = [[0] * M for _ in range(N)]
    t_list = [
        [[0, 0]],
        [[-1, 0], [0, -1], [1, 0], [0, 1]],
        [[1, 0], [-1, 0]],
        [[0, -1], [0, 1]],
        [[-1, 0], [0, 1]],
        [[0, 1], [1, 0]],
        [[0, -1], [1, 0]],
        [[0, -1], [-1, 0]]
    ]

    bfs(i, j, N, M, L)
    ans = 0
    for k in range(N):
        for l in range(M):
            if 0 < v[k][l] <= L:
                ans += 1
    print(f'#{tc} {ans}')