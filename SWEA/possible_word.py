T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    m = [list(map(int, input().split())) + [0] for _ in range(N)] + [[0] * (N+1)] #맵의 우측, 하단에 0을 추가

    cnt = 0
    for i in range(N):
        sum1 = 0
        sum2 = 0
        for j in range(N):
            sum1 += m[i][j]
            sum2 += m[j][i]

            if m[i][j+1] == 0: # 다음 순서로 0을 만났을 때 sum이 K 이면 cnt += 1, 아니면 sum을 초기화
                if sum1 == K:
                    cnt += 1
                sum1 = 0

            if m[j+1][i] == 0:
                if sum2 == K:
                    cnt += 1
                sum2 = 0

    print(f'#{tc} {cnt}')