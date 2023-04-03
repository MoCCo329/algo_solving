# 1028. 다이아몬드 광산  2023-04-03


N, M = map(int, input().split())
maps = [list(map(int, input())) for _ in range(N)]

limit = min(N, M) // 2 + (1 if min(N, M) % 2 == 1 else 0)

rDp = [[0] * M for _ in range(N)]
lDp = [[0] * M for _ in range(N)]

for i in range(N - 1, -1, -1):
    for j in range(M - 1, -1, -1):
        if maps[i][j] == 0: continue

        if i + 1 < N and j + 1 < M:
            rDp[i][j] = rDp[i + 1][j + 1] + 1
        else:
            rDp[i][j] = 1

        if i + 1 < N and j - 1 >= 0:
            lDp[i][j] = lDp[i + 1][j - 1] + 1
        else:
            lDp[i][j] = 1

for k in range(limit, 0, -1):
    flag = False

    for i in range(N - 2 * k + 1 + 1):
        for j in range(k - 1, M - k + 1):
            if rDp[i][j] >= k and rDp[i + k - 1][j - k + 1] >= k and lDp[i][j] >= k and lDp[i + k - 1][j + k - 1] >= k:
                print(k)
                exit(0)

print(0)