for T in range(int(input())):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    di = [0, 0, -1, 1]
    dj = [-1, 1, 0, 0]
    sum = 0

    for i in range(N):
        for j in range(N):
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0<=ni<N and 0<=nj<N:
                    if (arr[i][j] - arr[ni][nj]) >= 0:
                        sum += arr[i][j] - arr[ni][nj]
                    else:
                        sum += arr[ni][nj] - arr[i][j]
    print(f'#{T+1} {sum}')