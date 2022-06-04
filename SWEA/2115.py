def f(k, M, C, p):
    global ans, temp_ans

    if k == 2:
        if ans < p:
            ans = p
        return
    else:
        for i in range(N):
            for j in range(N-M+1):
                if sum(v[i][j:j+M]) == 0:
                    for l in range(M):
                        v[i][j+l] = 1
                    temp = arr[i][j:j+M]
                    if sum(temp) > C:
                        temp_ans = 0
                        ff(0, M, C, [], temp[:])
                    else:
                        temp_ans = sum([l**2 for l in temp])
                    f(k+1, M, C, p + temp_ans)
                    for l in range(M):
                        v[i][j+l] = 0


def ff(i, M, C, s, temp):
    global temp_ans

    if i == M:
        if sum(s) <= C:
            a = sum([j**2 for j in s])
            if a > temp_ans:
                temp_ans = a
            return
    elif sum(s) > C:
        return
    else:
        ff(i+1, M, C, s[:] + [temp[i]], temp[:])
        ff(i+1, M, C, s[:], temp[:])


T = int(input())
for tc in range(1, T+1):
    N, M, C = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    v = [[0] * N for _ in range(N)]
    ans = 0
    temp_ans = 0
    f(0, M, C, 0)
    print(f'#{tc} {ans}')