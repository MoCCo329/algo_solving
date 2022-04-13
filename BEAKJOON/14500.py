# 14500. 테트로미노 2022-04-13


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0

for i in range(N):
    for j in range(M):
        t = [0] * 19
        if j + 3 < M:
            t[0] = sum(arr[i][j:j + 4])
        if i + 3 < N:
            t[10] = arr[i][j] + arr[i + 1][j] + arr[i + 2][j] + arr[i + 3][j]
        if i + 2 < N and j + 1 < M:
            t[1] = sum(arr[i + 2][j:j + 2]) + arr[i][j] + arr[i + 1][j]
            t[3] = sum(arr[i + 1][j:j + 2]) + arr[i][j] + arr[i + 2][j + 1]
            t[6] = sum(arr[i][j:j + 2]) + arr[i + 1][j + 1] + arr[i + 2][j + 1]
            t[11] = sum(arr[i + 1][j:j + 2]) + arr[i][j + 1] + arr[i + 2][j + 1]
            t[12] = arr[i][j] + sum(arr[i + 1][j:j + 2]) + arr[i + 2][j]
            t[16] = sum(arr[i][j:j + 2]) + arr[i + 1][j] + arr[i + 2][j]
            t[17] = sum(arr[i + 2][j:j + 2]) + arr[i][j + 1] + arr[i + 1][j + 1]
            t[18] = sum(arr[i + 1][j:j + 2]) + arr[i][j + 1] + arr[i + 2][j]
        if i + 1 < N and j + 1 < M:
            t[2] = sum(arr[i][j:j + 2]) + sum(arr[i + 1][j:j + 2])
        if i + 1 < N and j + 2 < M:
            t[4] = sum(arr[i][j:j + 3]) + arr[i + 1][j + 1]
            t[5] = sum(arr[i][j:j + 3]) + arr[i + 1][j]
            t[7] = sum(arr[i + 1][j:j + 3]) + arr[i][j + 2]
            t[8] = sum(arr[i][j + 1:j + 3]) + sum(arr[i + 1][j:j + 2])
            t[9] = sum(arr[i + 1][j:j + 3]) + arr[i][j + 1]
            t[13] = arr[i][j] + sum(arr[i + 1][j:j + 3])
            t[14] = sum(arr[i][j:j + 3]) + arr[i + 1][j + 2]
            t[15] = sum(arr[i][j:j + 2]) + sum(arr[i + 1][j + 1:j + 3])

        for k in range(19):
            if t[k] > ans:
                ans = t[k]

print(ans)