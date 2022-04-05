# 1949. 등산로 조성 2022-04-05

def dfs(i, j, N, K, cnt):
    global ans
    if ans < cnt + 1:
        ans = cnt + 1
    for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        ni, nj = i + di, j + dj
        if 0 <= ni < N and 0 <= nj < N and v[ni][nj] == 0:
            v[ni][nj] = 1
            if arr[i][j] > arr[ni][nj]:
                dfs(ni, nj, N, K, cnt + 1)
            elif arr[i][j] > arr[ni][nj] - K:
                temp = arr[ni][nj]
                arr[ni][nj] = arr[i][j] - 1
                dfs(ni, nj, N, 0, cnt + 1)
                arr[ni][nj] = temp
            v[ni][nj] = 0


T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    v = [[0] * N for _ in range(N)]
    ans = 0

    H = 0
    for i in range(N):
        for j in range(N):
            if H < arr[i][j]:
                H = arr[i][j]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == H:
                v[i][j] = 1
                dfs(i, j, N, K, 0)
                v[i][j] = 0

    print(f'#{tc} {ans}')