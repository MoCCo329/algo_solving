# 1799. 비숍  2022-07-29


# 시간초과

def dfs(k, end, cnt):
    global ans
    if k == end:
        ans = max(ans, cnt)
        return

    if ans - cnt > (end - k) * 2:
        return

    for i in range(k, end):
        if not v[available[i][0]] and not v[available[i][1]]:
            v[available[i][0]] = 1
            v[available[i][1]] = 1
            dfs(i + 1, end, cnt + 1)
            v[available[i][0]] = 0
            v[available[i][1]] = 0


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
v = [0] * (4 * N - 2)

available = []
for i in range(N):
    for j in range(N):
        if arr[i][j]:
            available.append((i + j, - j + i + 3 * N - 2))

available.sort()
ans = 1
dfs(0, len(available), 0)
print(ans)