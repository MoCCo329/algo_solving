def f(i, k, N, ans):  # i곳 방문했으며 이전에 k를 방문, ans는 소비량 합
    global minV
    if i == N:
        ans += arr[k][0]
        if minV > ans:
            minV = ans
    else:
        for j in range(N):
            if v[j] == 0:
                v[j] = 1
                f(i+1, j, N, ans + arr[k][j])
                v[j] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    v = [0] * N
    minV = 100 * N
    v[0] = 1
    f(1, 0, N, 0)
    print(f'#{tc} {minV}')