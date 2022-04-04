T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_kill = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            kill = 0

            for k in range(M): # 정대각선 방향과 역대각선방향으로 검사
                kill += arr[i+k][j+k]
                kill += arr[i+M-1-k][j+k]
            if M%2 == 1: # M이 홍수이면 가운데 겹치는부분 고려
                kill -= arr[i + M//2][j + M//2]

            if kill > max_kill:
                max_kill = kill

    print(f'#{tc} {max_kill}')