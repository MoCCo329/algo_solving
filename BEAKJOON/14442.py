# 14442. 벽 부수고 이동하기 2  2023-02-03


from collections import deque


def bfs():
    v = [[-1] * M for _ in range(N)]
    v[0][0] = K
    q = deque()
    q.append((0, 0, 1))

    while q:
        i, j, cnt = q.popleft()
        if i == N - 1 and j == M - 1:
            return cnt

        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ni, nj = i + di, j + dj
            if ni < 0 or ni >= N or nj < 0 or nj >= M: continue

            if v[ni][nj] == -1:
                if maps[ni][nj] == 1 and v[i][j] > 0:
                    v[ni][nj] = v[i][j] - 1
                    q.append((ni, nj, cnt + 1))
                elif maps[ni][nj] == 0:
                    v[ni][nj] = v[i][j]
                    q.append((ni, nj, cnt + 1))
            else:
                if maps[ni][nj] == 1 and v[ni][nj] < v[i][j] - 1:
                    v[ni][nj] = v[i][j] - 1
                    q.append((ni, nj, cnt + 1))
                elif maps[ni][nj] == 0 and v[ni][nj] < v[i][j]:
                    v[ni][nj] = v[i][j]
                    q.append((ni, nj, cnt + 1))

    return -1


N, M, K = map(int, input().split())
maps = [list(map(int, input())) for _ in range(N)]
print(bfs())