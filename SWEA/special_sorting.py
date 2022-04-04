T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    new_arr = [0] * N

    for i in range(N-1, 0, -1): # 버블 정렬
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    for i in range(N//2): # new_arr에 큰 수 작은 수 넣기
        new_arr[2*i] = arr[-i-1]
        new_arr[2*i + 1] = arr[i]

    print(f'#{tc}', *new_arr[0:10])