# 15683. 감시 2022-04-16


def dfs(cnt, L):
    global ans
    if cnt == L:
        cnt = 0
        for i in range(N):
            for j in range(M):
                if arr[i][j] == 0:
                    cnt += 1
        if ans > cnt:
            ans = cnt
    else:
        i, j = cctvs[cnt][:2]
        arr[i][j] = 1
        if cctvs[cnt][2] == 1:
            for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                v = []
                ni, nj = i + di, j + dj
                while 0 <= ni < N and 0 <= nj < M and arr[ni][nj] != 6:
                    if arr[ni][nj] == 0:
                        arr[ni][nj] = -1
                        v.append([ni, nj])
                    ni, nj = ni + di, nj + dj
                dfs(cnt + 1, L)
                for vi, vj in v:
                    arr[vi][vj] = 0
        if cctvs[cnt][2] == 2:
            for di1, dj1, di2, dj2 in [[0, -1, 0, 1], [-1, 0, 1, 0]]:
                v = []
                ni, nj = i + di1, j + dj1
                while 0 <= ni < N and 0 <= nj < M and arr[ni][nj] != 6:
                    if arr[ni][nj] == 0:
                        arr[ni][nj] = -1
                        v.append([ni, nj])
                    ni, nj = ni + di1, nj + dj1
                ni, nj = i + di2, j + dj2
                while 0 <= ni < N and 0 <= nj < M and arr[ni][nj] != 6:
                    if arr[ni][nj] == 0:
                        arr[ni][nj] = -1
                        v.append([ni, nj])
                    ni, nj = ni + di2, nj + dj2
                dfs(cnt + 1, L)
                for vi, vj in v:
                    arr[vi][vj] = 0
        if cctvs[cnt][2] == 3:
            for di1, dj1, di2, dj2 in [[-1, 0, 0, 1], [0, 1, 1, 0], [1, 0, 0, -1], [0, -1, -1, 0]]:
                v = []
                ni, nj = i + di1, j + dj1
                while 0 <= ni < N and 0 <= nj < M and arr[ni][nj] != 6:
                    if arr[ni][nj] == 0:
                        arr[ni][nj] = -1
                        v.append([ni, nj])
                    ni, nj = ni + di1, nj + dj1
                ni, nj = i + di2, j + dj2
                while 0 <= ni < N and 0 <= nj < M and arr[ni][nj] != 6:
                    if arr[ni][nj] == 0:
                        arr[ni][nj] = -1
                        v.append([ni, nj])
                    ni, nj = ni + di2, nj + dj2
                dfs(cnt + 1, L)
                for vi, vj in v:
                    arr[vi][vj] = 0
        if cctvs[cnt][2] == 4:
            for di1, dj1, di2, dj2, di3, dj3 in [[-1, 0, 0, 1, 1, 0], [0, 1, 1, 0, 0, -1], [1, 0, 0, -1, -1, 0], [0, -1, -1, 0, 0, 1]]:
                v = []
                ni, nj = i + di1, j + dj1
                while 0 <= ni < N and 0 <= nj < M and arr[ni][nj] != 6:
                    if arr[ni][nj] == 0:
                        arr[ni][nj] = -1
                        v.append([ni, nj])
                    ni, nj = ni + di1, nj + dj1
                ni, nj = i + di2, j + dj2
                while 0 <= ni < N and 0 <= nj < M and arr[ni][nj] != 6:
                    if arr[ni][nj] == 0:
                        arr[ni][nj] = -1
                        v.append([ni, nj])
                    ni, nj = ni + di2, nj + dj2
                ni, nj = i + di3, j + dj3
                while 0 <= ni < N and 0 <= nj < M and arr[ni][nj] != 6:
                    if arr[ni][nj] == 0:
                        arr[ni][nj] = -1
                        v.append([ni, nj])
                    ni, nj = ni + di3, nj + dj3
                dfs(cnt + 1, L)
                for vi, vj in v:
                    arr[vi][vj] = 0
        if cctvs[cnt][2] == 5:
            for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                ni, nj = i + di, j + dj
                while 0 <= ni < N and 0 <= nj < M and arr[ni][nj] != 6:
                    arr[ni][nj] = -1
                    ni, nj = ni + di, nj + dj
            dfs(cnt + 1, L)

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
cctvs = []

for i in range(N):
    for j in range(M):
        if arr[i][j] != 6 and arr[i][j] != 0:
            cctvs.append([i, j, arr[i][j]])
            arr[i][j] = 0
L = len(cctvs)
ans = N * M
dfs(0, L)

print(ans)