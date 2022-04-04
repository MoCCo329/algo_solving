T = int(input())
for tc in range(1, T+1):
    N = int(input())
    c_arr = list(map(int, input().split()))

    k = 1
    max_num = 0
    carrot = c_arr[0]
    for i in range(1, len(c_arr)):
        if c_arr[i] - carrot == 1:
            k += 1
            carrot = c_arr[i]
        else:
            k = 1
            carrot = c_arr[i]

        if k > max_num:
            max_num = k

    print(f'#{tc} {max_num}')