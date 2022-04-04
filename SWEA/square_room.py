def f(i, j):
    global ans, cnt
    origin = [i, j]
    while True:
        cnt += 1
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i+di, j+dj
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] - arr[i][j] == 1:
                i, j = ni, nj
                break
        else:
            if cnt > ans[0]:
                ans[0] = cnt
                ans[1] = [origin[0], origin[1]]
            elif cnt == ans[0]:
                if arr[ans[1][0]][ans[1][1]] > arr[origin[0]][origin[1]]:
                    ans[1] = [origin[0], origin[1]]
            cnt = 0
            return
                
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = [0, []]
    cnt = 0

    for i in range(N):
        for j in range(N):
            f(i, j)

    print(f'#{tc} {arr[ans[1][0]][ans[1][1]]} {ans[0]}')