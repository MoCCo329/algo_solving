# 1113. 수영장 만들기  2022-07-16


from collections import deque
N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]

ans = 0
for k in range(1, 9):
    v = [[0] * M for _ in range(N)]
    for i in range(1, N - 1):
        for j in range(1, M - 1):
            if arr[i][j] <= k and v[i][j] == 0:
                chk = 0
                q = deque()
                q.append((i, j))
                v[i][j] = 1
                temp_ans = 1
                while q:
                    ii, jj = q.popleft()
                    for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                        ni, nj = ii + di, jj + dj
                        if ni == 0 or ni == N - 1 or nj == 0 or nj == M - 1:
                            if arr[ni][nj] <= k:
                                chk = 1
                                continue
                            else:
                                continue
                        if arr[ni][nj] <= k and v[ni][nj] == 0:
                            temp_ans += 1
                            q.append((ni, nj))
                            v[ni][nj] = 1
                if chk == 0:
                    ans += temp_ans

print(ans)