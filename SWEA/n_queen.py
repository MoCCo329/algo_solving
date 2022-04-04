def f(i, N):
    global ans

    if i == N:
        ans += 1
    else:
        for j in range(N):
            if arr_h[j] == 0 and arr_lc[i + j] == 0 and arr_rc[N - 1 - i + j] == 0:
                arr_h[j] = 1
                arr_lc[i + j] = 1
                arr_rc[N - 1 - i + j] = 1
                f(i+1, N)
                arr_h[j] = 0
                arr_lc[i + j] = 0
                arr_rc[N - 1 - i + j] = 0
        else:
            return

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr_h = [0] * N
    arr_rc = [0] * (2*N-1)
    arr_lc = [0] * (2*N-1)
    ans = 0
    f(0, N)
    print(f'#{tc} {ans}')