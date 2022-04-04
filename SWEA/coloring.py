T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    new_arr = [[0]*10 for _ in range(10)]
    cnt = 0

    for l in arr:
        for i in range(l[0], l[2]+1):
            for j in range(l[1], l[3]+1):
                new_arr[i][j] += l[-1]
                if new_arr[i][j] == 3:
                    cnt += 1

    print(f'#{tc} {cnt}')