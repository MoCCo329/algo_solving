T = int(input())
for tc in range(1, T+1):
    arr = [list(input()) for _ in range(5)]

    arr_len = []
    max_len = len(arr[0])
    for str in arr:
        arr_len += [len(str)]
        if max_len < len(str):
            max_len = len(str)

    for i in range(5):
        arr[i] += [''] * (max_len - arr_len[i])

    answer = ''
    for j in range(max_len):
        for i in range(5):
            answer += arr[i][j]

    print(f'#{tc} {answer}')