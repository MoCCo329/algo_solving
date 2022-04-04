for T in range(1,11):
    tc = int(input())

    arr = [list(map(int, input().split())) for _ in range(100)]
    sum_list = []

    subsum3 = 0
    subsum4 = 0

    for i in range(100):
        subsum1 = 0
        subsum2 = 0
        for j in range(100):
            subsum1 += arr[i][j]
            subsum2 += arr[j][i]
        sum_list += [subsum1, subsum2]

        subsum3 += arr[i][i]
        subsum4 += arr[i][99-i]

    sum_list += [subsum3, subsum4]
    max_test = sum_list[0]

    for sum in sum_list:
        if max_test < sum:
            max_test = sum

    print(f'#{tc} {max_test}')