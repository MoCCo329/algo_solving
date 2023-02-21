# 1520. 내리막 길  2023-02-21


def dfs(i, j):
    if i == N - 1 and j == M - 1: return 1
    if vis[i][j] != -1: return vis[i][j]

    vis[i][j] = 0
    for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        ni, nj = i + di, j + dj
        if not (0 <= ni < N) or not (0 <= nj < M) or maps[i][j] <= maps[ni][nj]: continue

        vis[i][j] += dfs(ni, nj)

    return vis[i][j]


N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
vis = [[-1] * M for _ in range(N)]
dfs(0, 0)

print(vis[0][0])