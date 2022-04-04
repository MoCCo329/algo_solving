def cor(i, L):  # 2진수 i번째 수 고치기
    N = 0
    for j in range(L):
        if j == i:
            N += ((int(bi[-j-1]) + 1) % 2) * 2**j
        else:
            N += int(bi[-j-1]) * 2**j
    return N

T = int(input())
for tc in range(1, T+1):
    bi = input()
    tr = input()
    L = len(bi)

    M = 0
    for i in range(len(tr)):
        M += int(tr[-i-1]) * 3**i

    for i in range(L):
        N = cor(i, L)
        dif = abs(N - M)

        for j in range(len(tr)):
            if dif == 0 or dif == 3**j or dif == 2 * 3**j:
                print(f'#{tc} {N}')