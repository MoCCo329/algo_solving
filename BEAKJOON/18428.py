# 18428. 감시 피하기  2022-07-16


def dfs(k, step):
    global ans
    if ans == "YES":
        return

    if k == 3:
        for i in range(N):
            for j in range(N):
                if arr[i][j] == "T":
                    for di, dj in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
                        l = 1
                        while True:
                            ni, nj = i + l * di, j + l * dj
                            if 0 > ni or N <= ni or 0 > nj or N <= nj:
                                break
                            if arr[ni][nj] == "O" or arr[ni][nj] == "T":
                                break
                            if arr[ni][nj] == "S":
                                return
                            l += 1
        ans = "YES"

    else:
        for s in range(step + 1, N ** 2):
            i = s // N
            j = s % N
            if arr[i][j] == "X":
                arr[i][j] = "O"
                dfs(k + 1, s)
                arr[i][j] = "X"


N = int(input())
arr = [list(input().split()) for _ in range(N)]

ans = "NO"
dfs(0, -1)
print(ans)