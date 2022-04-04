T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    answer = ''

    for i in range(N): # 가로
        for j in range(N-M+1):
            for k in range(M//2):
                if arr[i][j+k] == arr[i][j+M-1-k]:
                    pass
                else:
                    break
            else: # k for문 잘 수행되면 답저장
                for k in range(M):
                    answer += arr[i][j+k]

    for j in range(N): # 세로
        for i in range(N-M+1):
            for k in range(M//2):
                if arr[i+k][j] == arr[i+M-1-k][j]:
                    pass
                else:
                    break
            else:
                for k in range(M):
                    answer += arr[i+k][j]

    print(f'#{tc} {answer}')