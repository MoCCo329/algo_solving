T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    new_arr = [[0]*N for _ in range(N)]
    answer = [[0]*3 for _ in range(N)]

    for d in range(3):
        for i in range(N): # N*N 돌면서 new_arr에 90도 회전해서 담기
            for j in range(N):
                new_arr[i][j] = arr[N-1-j][i]

        for i in range(N): # 정답 담기
            answer[i][d] = ''.join(map(str, new_arr[i]))

        for i in range(N): # 다음 90도 돌리기를 위해 arr에 new_arr deep copy
            for j in range(N):
                arr[i][j] = new_arr[i][j]

    print(f'#{tc}')
    for i in range(N):
        print(*answer[i])