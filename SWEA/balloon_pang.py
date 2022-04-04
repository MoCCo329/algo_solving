T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans_list = []

    for i in range(N):
        for j in range(M):
            temp = -arr[i][j]
            for k in range(-arr[i][j], arr[i][j]+1):
                if 0 <= i+k < N:
                    temp += arr[i+k][j]
                if 0 <= j+k < M:
                    temp += arr[i][j+k]

            ans_list += [temp]

    maxV = ans_list[0]
    for V in ans_list:
        if maxV < V:
            maxV = V

    print(f'#{tc} {maxV}')