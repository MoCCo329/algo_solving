def f(i, j, k):
    cnt = 0
    for ni in range(N):
        for nj in range(N):
            if arr[ni][nj] == 1 and abs(i - ni) + abs(j - nj) < k:
                cnt += 1
    if 2 * k**2 - 2 * k + 1 <= cnt * M:
        return cnt
    else:
        return 0

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = []

    for i in range(N):
        for j in range(N):
            k = 1
            while k <= N+1:
                ans += [f(i, j, k)]
                k += 1

    print(f'#{tc} {max(ans)}')