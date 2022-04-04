def f(i, j, N, K, cnt):


T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    v = [[0] * N for _ in range(N)]
    ans = 0

    H = 0
    for i in range(N):
        for j in range(N):
            if H < arr[i][j]:
                H = arr[i][j]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == H:
                f(i, j, N, K, 0)

    print(f'#{tc} {ans}')