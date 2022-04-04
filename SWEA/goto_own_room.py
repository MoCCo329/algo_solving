T = int(input())
for tc in range(1, T+1):
    counts = [0] * 200
    for _ in range(int(input())):
        N, M = map(int, input().split())

        if M < N: # N을 작은수로
            N, M = M, N

        for i in range((N-1)//2, (M-1)//2 + 1): # 지나가야 하는 길에 + 1
            counts[i] += 1

    max_temp = counts[0] # 최대 겹치는 수
    for c in counts:
        if max_temp < c:
            max_temp = c

    print(f'#{tc} {max_temp}')