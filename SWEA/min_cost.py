def f(i, N, p):
    global ans

    if p > ans:
        return
    if i == N:
        ans = p
        return
    else:
        for j in range(N):
            if v[j] == 0:
                v[j] = 1
                f(i+1, N, p + arr[i][j])
                v[j] = 0
        return

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    v = [0] * N
    ans = sum([arr[i][i] for i in range(N)])
    f(0, N, 0)
    print(f'#{tc} {ans}')

