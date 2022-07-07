# 18430. 무기공학 2022-07-07


d_list = [([1, 0], [0, 1]), ([1, 0], [0, -1]), ([0, -1], [-1, 0]), ([-1, 0], [0, 1])]


def dfs(i, j, p):
    global ans
    if j == M:
        i += 1
        j = 0
    if i >= N or j >= M:
        if ans < p:
            ans = p
    else:
        if not v[i][j]:
            v[i][j] = 1
            for d in d_list:
                temp1 = arr[i][j] * 2
                temp2 = []
                for di, dj in d:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < N and 0 <= nj < M and v[ni][nj] == 0:
                        temp1 += arr[ni][nj]
                        temp2.append((ni, nj))
                    else:
                        break
                else:
                    for ni, nj in temp2:
                        v[ni][nj] = 1
                    dfs(i, j + 1, p + temp1)
                    for ni, nj in temp2:
                        v[ni][nj] = 0
            v[i][j] = 0
        dfs(i, j + 1, p)


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0
max_k = 0
v = [[0] * M for _ in range(N)]

dfs(0, 0, 0)
print(ans)