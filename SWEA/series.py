T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(len, input().split('0')))

    max_len = arr[0]
    for l in arr:
        if max_len < l:
            max_len = l

    print(f'#{tc} {max_len}')