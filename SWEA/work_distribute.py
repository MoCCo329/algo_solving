def dfs(i, N, s):
    global ans
    if i == N:
        if s > ans:
            ans = s
    elif s <= ans:
        return
    else:
        for j in range(N):
            if v[j] == 0:
                v[j] = 1
                dfs(i+1, N, s*arr[i][j]/100)
                v[j] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    v = [0] * N
    ans = 0
    dfs(0, N, 1)
    print(f'#{tc} {round(ans*100, 6):.6f}')