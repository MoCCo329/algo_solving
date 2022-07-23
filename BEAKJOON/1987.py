# 1987. 알파벳  2022-07-23


from collections import deque

N, M = map(int, input().split())
arr = [list(map(lambda x: ord(x) - 65, input())) for _ in range(N)]
v = [[set() for _ in range(M)] for _ in range(N)]

ans = 1
q = deque()
q.append((0, 0, 1, 1 << arr[0][0]))
while q:
    i, j, cnt, path = q.popleft()
    ans = max(ans, cnt)

    for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
        ni, nj = i + di, j + dj
        if 0 <= ni < N and 0 <= nj < M:
            if path & 1 << arr[ni][nj] or path | 1 << arr[ni][nj] in v[ni][nj]:
                continue
            v[ni][nj].add(path | 1 << arr[ni][nj])
            q.append((ni, nj, cnt + 1, path | 1 << arr[ni][nj]))
print(ans)