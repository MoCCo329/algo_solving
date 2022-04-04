for tc in range(1, int(input())+1):
    N = int(input())
    arr = list(map(int, input().split()))

    max_num = arr[0]
    for i in range(1, N): # 최댓값 찾기
        if max_num < arr[i]:
            max_num = arr[i]

    print(f'#{tc} {max_num}')