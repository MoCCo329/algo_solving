def f(i, j, N, ans):
    global minV
    if i == N-1 and j == N-1:
        ans += arr[i][j]
        if minV > ans:
            minV = ans
        return
    else:
        if i >= N or j >= N:
            return
        else:
            ans += arr[i][j]
        if i < N-1:
            f(i+1, j, N, ans)
        if j < N-1:
            f(i, j+1, N, ans)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    minV = sum(arr[0] + arr[1:N][-1])
    f(0, 0, N, 0)
    print(f'#{tc} {minV}')