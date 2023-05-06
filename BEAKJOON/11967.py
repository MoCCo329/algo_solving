# 11967. 불켜기  2023-05-06


from collections import deque


N, K = map(int, input().split())
switches = [[[] for _ in range(N + 1)] for _ in range(N + 1)]
vis = [[0] * (N + 1) for _ in range(N + 1)]  # 0 이면 불가 1이면 방문가능 2이면 이미 방문
is_on = [[False] * (N + 1) for _ in range(N + 1)]

for _ in range(K):
    x, y, a, b = map(int, input().split())
    switches[x][y].append((a, b))

is_on[1][1] = True
vis[1][1] = 0

ans = 1
q = deque()
q.append((1, 1))
while q:
    i, j = q.popleft()

    for a, b in switches[i][j]:
        if not is_on[a][b]:
            is_on[a][b] = True
            ans += 1
            if vis[a][b] == 1:
                vis[a][b] = 2
                q.append((a, b))

    for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        ni, nj = i + di, j + dj
        if not (0 < ni <= N) or not (0 < nj <= N): continue
        if vis[ni][nj] == 0:
            vis[ni][nj] = 1
            if is_on[ni][nj]:
                vis[ni][nj] = 2
                q.append((ni, nj))

print(ans)