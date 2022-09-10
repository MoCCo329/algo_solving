# 2206. 벽 부수고 이동하기  2022-09-10


from collections import deque


N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
v = [[0] * M for _ in range(N)]  # cnt 가 있는 상태로 방문하면 2, 없는 상태로 방문하면 1. 2이면 더 방문할 필요 없다.
v[0][0] = 2

q = deque()
q.append((0, 0, 1, 1))
ans = -1
while q:
    i, j, cnt, path = q.popleft()
    if (i, j) == (N - 1, M - 1):
        ans = path
        break

    for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        ni, nj = i + di, j + dj
        if 0 <= ni < N and 0 <= nj < M and (v[ni][nj] == 0 or (cnt and v[ni][nj] == 1)):
            if arr[ni][nj] and cnt and not v[ni][nj]:
                v[ni][nj] = 1
                q.append((ni, nj, cnt - 1, path + 1))
            if not arr[ni][nj]:
                if cnt:
                    v[ni][nj] = 2
                else:
                    v[ni][nj] = 1
                q.append((ni, nj, cnt, path + 1))

print(ans)