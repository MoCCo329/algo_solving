# 26076. 곰곰이의 식단 관리 2  2023-04-03


from collections import deque


N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
vis = [[0] * M for _ in range(N)]
vis[0][0] = 1
vis[N - 1][M - 1] = 1
q = deque()

for j in range(1, M):
    if maps[0][j] == 0:
        vis[0][j] = 2
        q.append((0, j, 2))
    else:
        vis[0][j] = 1
        q.appendleft((0, j, 1))
for i in range(1, N - 1):
    if maps[i][M - 1] == 0:
        vis[i][M - 1] = 2
        q.append((i, M - 1, 2))
    else:
        vis[i][M - 1] = 1
        q.appendleft((i, M - 1, 1))

while q:
    i, j, n = q.popleft()

    for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]:
        ni, nj = i + di, j + dj
        if not (0 <= ni < N) or not (0 <= nj < M) or vis[ni][nj] != 0: continue

        if maps[ni][nj] == 1:
            vis[ni][nj] = n
            q.appendleft((ni, nj, n))
        else:
            vis[ni][nj] = n + 1
            q.append((ni, nj, n + 1))

ans = 2
for i in range(1, N):
    ans = min(ans, vis[i][0] - 1)
for j in range(1, M - 1):
    ans = min(ans, vis[N - 1][j] - 1)

print(ans)