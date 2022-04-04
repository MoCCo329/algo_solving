for T in range(int(input())):
    N, Q = map(int, input().split())
    N_list = [0] * N

    for i in range(Q):
        L, R = map(int, input().split())
        for j in range(R-L+1):
            N_list[L + j - 1] = i+1

    print(f'#{T+1}', end=' ')
    print(*N_list)