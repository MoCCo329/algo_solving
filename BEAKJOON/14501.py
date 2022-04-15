# 14501. 퇴사 2022-04-15


def dfs(i, p):
    global ans
    if i == N:
        if ans < p:
            ans = p
    else:
        if i + arr[i][0] <= N:
            dfs(i + arr[i][0], p + arr[i][1])
        dfs(i + 1, p)


N = int(input())
arr = [0] * N
for i in range(N):
    arr[i] = list(map(int, input().split()))

ans = 0
dfs(0, 0)
if arr[0][0] <= N:
    dfs(arr[0][0], arr[0][1])

print