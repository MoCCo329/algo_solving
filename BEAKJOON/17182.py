# 17182. 우주 탐사선 2022-07-12


def dfs(k, now, p):
    global ans
    if k == N:
        ans = min(ans, p)
        return
    elif ans < p:
        return
    else:
        for i in range(N):
            if v[i] == 0:
                v[i] = 1
                dfs(k + 1, i, p + adj_arr[now][i])
                v[i] = 0


N, start = map(int, input().split())
adj_arr = [list(map(int, input().split())) for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            if i == j: continue
            if adj_arr[i][j] > adj_arr[i][k] + adj_arr[k][j]:
                adj_arr[i][j] = adj_arr[i][k] + adj_arr[k][j]

ans = 1001 * N
v = [0] * N
v[start] = 1
dfs(1, start, 0)
print(ans)