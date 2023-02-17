# 1201. NMK  2023-02-17


N, M, K = map(int, input().split())

if not (M + K - 1 <= N <= M * K): print(-1)
else:
    arr = [1] * M
    arr[M - 1] += K - 1
    N -= M + K - 1
    for i in range(M - 1):
        arr[i] += min(K - 1, N)
        N -= K - 1
        if N <= 0: break

    t = 0
    for i in range(M):
        t += arr[i]
        for j in range(t, t - arr[i], -1):
            print(j, end=' ')
    print()