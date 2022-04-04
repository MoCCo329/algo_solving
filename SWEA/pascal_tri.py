def pascal_tri(arr, N, k): # 재귀함수로 풀기
    temp = []

    if k > 2:
        temp += [1]
        for i in range(len(arr[-1])-1):
            temp += [arr[-1][i] + arr[-1][i+1]]
        temp += [1]
        arr += [temp]
    elif k == 2:
        arr += [[1, 1]]
    else:
        arr += [[1]]

    if k == N:
        return arr
    else:
        return pascal_tri(arr, N, k+1)

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    answer = pascal_tri([], N, 1)

    print(f'#{tc}')
    for line in answer:
        print(*line)