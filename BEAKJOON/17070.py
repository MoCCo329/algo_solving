# 17070. 파이프 옮기기 1  2022-09-09


def dfs(i, j, s):  # i, j 는 파이프 위치, s는 state로 1이면 가로 2면 세로, 3이면 대각선
    global ans

    if i == N - 1 and j == N - 1:
        ans += 1
        return
    
    if s == 1 or s == 3:
        if j + 1 < N and not arr[i][j + 1]:
            dfs(i, j + 1, 1)
    if s == 2 or s == 3:
        if i + 1 < N and not arr[i + 1][j]:
            dfs(i + 1, j, 2)
    if i + 1 < N and j + 1 < N and not arr[i + 1][j] and not arr[i + 1][j + 1] and not arr[i][j + 1]:
        dfs(i + 1, j + 1, 3)

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

ans = 0
dfs(0, 1, 1)
print(ans)