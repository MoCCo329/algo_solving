def f(i, N, s): # 행, 배열 크기, 부분합
    global minV
    if i == N:
        s = 0
        for j in range(N):
            s += arr[j][p[j]]
        if minV > s:
            minV = s
    elif minV != 1000 and s >= minV:
        return
    else:
        for j in range(i, N):
            p[i], p[j] = p[j], p[i]
            f(i+1, N, s + arr[i][p[i]])
            p[i], p[j] = p[j], p[i]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    minV = 1000
    p = [i for i in range(N)]
    f(0, N, 0)
    print(f'#{tc} {minV}')