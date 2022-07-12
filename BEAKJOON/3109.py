# 3109. 빵집  2022-07-13


def dfs(i, j):
    arr[i][j] = "X"

    if j == M - 1:
        return True
    for d in [-1, 0, 1]:
        if 0 <= i + d < N and arr[i + d][j + 1] == ".":
            if dfs(i + d, j + 1):
                return True
    return False


N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
ans = 0

for i in range(N):
    if arr[i][0] == "." and dfs(i, 0):
        ans += 1

print(ans)