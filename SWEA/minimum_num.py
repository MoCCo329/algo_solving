for tc in range(1, int(input())+1):
    N = int(input())
    arr = list(map(int, input().split()))

    min_idx = 0 # 최솟값 인덱스
    for i in range(1, N): # 최솟값 인덱스 저장
        if arr[min_idx] > arr[i]:
            min_idx = i

    print(f'#{tc} {min_idx+1}')