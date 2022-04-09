# 14503. 로봇 청소기 2022-04-09

d_list = [[-1, 0], [0, 1], [1, 0], [0, -1]]  # 0부터 북 동 남 서
def dfs(i, j, d, k):
    if k == 4:
        di, dj = d_list[d]
        ni, nj = i - di, j - dj
        if arr[ni][nj] == 1:
            return
        else:
            dfs(ni, nj, d, 0)

    else:
        d = (d - 1) % 4
        di, dj = d_list[d]
        ni, nj = i + di, j + dj
        if arr[ni][nj] == 0:  # 왼쪽이 청소 안한경우
            arr[ni][nj] = -1
            dfs(ni, nj, d, 0)
        else:
            dfs(i, j, d, k + 1)
    return


N, M = map(int, input().split())
si, sj, sd = list(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(N)]

arr[si][sj] = -1
dfs(si, sj, sd, 0)
ans = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == -1:
            ans += 1

print(ans)