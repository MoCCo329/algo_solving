def f(i, N, K, S):
    if K == S:
        for j in range(N):
            if bit[j]:
                print(a[j], end=' ')
        print()
        # return
    elif i == N:
        return
    elif S > K:
        return
    else:
        bit[i] = 1
        f(i+1, N, K, S+a[i])
        bit[i] = 0
        f(i+1, N, K, S)

N = 10
a = [x for x in range(1, N+1)]
bit = [0]*N
K = 10
f(0, N, K, 0)