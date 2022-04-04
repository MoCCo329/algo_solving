T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_len = 0 # 길이 저장

    for i in range(N):
        k = 0
        for j in range(M-1):
            if arr[i][j] == 1 and arr[i][j+1] == 1: # 다음것과 1이 연속되면 k증가
                k += 1
            else: # 연속되지 않으면 k초기화
                k = 0

            if max_len < k+1: # 최댓값 저자
                max_len = k+1

    for j in range(M): # 수직방향도 마찬가지
        k = 0
        for i in range(N-1):
            if arr[i][j] == 1 and arr[i+1][j] == 1:
                k += 1
            else:
                k = 0

            if max_len < k+1:
                max_len = k+1

    print(f'#{tc} {max_len}')