T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    w = list(map(int, input().split()))
    t = list(map(int, input().split()))
    v = [0] * N
    ans = 0

    for tt in t:
        idx = -1
        for i in range(N):
            if tt - w[i] >= 0 and v[i] == 0:
                if idx == -1:
                    idx = i
                else:
                    if w[idx] < w[i]:
                        idx = i

        if idx != -1:
            ans += w[idx]
            v[idx] = 1

    print(f'#{tc} {ans}')