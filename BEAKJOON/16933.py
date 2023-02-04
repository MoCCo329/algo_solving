# 16933. 벽 부수고 이동하기 3  2023-02-04


from collections import deque


N, M, K = map(int, input().split())
maps = [list(map(int, input())) for _ in range(N)]

v = [[-1] * M for _ in range(N)]
v[0][0] = K
q = deque()
q.append((0, 0, 1, K))
ans = -1

while q:
    i, j, cnt, k = q.popleft()
    if i == N - 1 and j == M - 1:
        ans = cnt
        break

    for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        ni, nj = i + di, j + dj
        if not (0 <= ni < N) or not (0 <= nj < M): continue

        if v[ni][nj] == -1:
            if maps[ni][nj] == 0:
                v[ni][nj] = k
                q.append((ni, nj, cnt + 1, k))
            elif maps[ni][nj] == 1 and k > 0:
                if cnt % 2 == 1:
                    v[ni][nj] = k - 1
                    q.append((ni, nj, cnt + 1, k - 1))
                else:
                    q.append((i, j, cnt + 1, k))
        else:
            if maps[ni][nj] == 0:
                if v[ni][nj] < k:
                    v[ni][nj] = k
                    q.append((ni, nj, cnt + 1, k))
            elif maps[ni][nj] == 1 and v[ni][nj] < k - 1:
                if cnt % 2 == 1:
                    v[ni][nj] = k - 1
                    q.append((ni, nj, cnt + 1, k - 1))
                else:
                    q.append((i, j, cnt + 1, k))

print(ans)
