T = int(input())
for tc in range(1,T+1):
    N = int(input())
    NN = N**2                                       #최대 숫자
    new_arr = [[0]*N for _ in range(N)]             #새로운 배열을 담을 arr

    d_list = [[0, 1], [1, 0], [0, -1], [-1, 0]] * N #4가지 방향. 넉넉히 N곱해준다. 원래 필요한 dk 수는 (N*2-1)/4
    dk = 0
    ni = 0
    nj = 0
    k = 1

    while k <= NN:
        if 0<=ni+d_list[dk][0]<N and 0<=nj+d_list[dk][1]<N and new_arr[ni+d_list[dk][0]][nj+d_list[dk][1]] == 0: #다음 칸이 범위를 안넘어가면 그대로 new_arr에 k입력
            new_arr[ni][nj] = k
            k += 1
            ni += d_list[dk][0]
            nj += d_list[dk][1]

        else: #다음 칸이 범위를 넘어가면 dk += 1 하여 방향을 전환
            new_arr[ni][nj] = k
            k += 1
            dk += 1
            ni += d_list[dk][0]
            nj += d_list[dk][1]

    print(f'#{tc}')
    for i in range(N):
        print(*new_arr[i])
