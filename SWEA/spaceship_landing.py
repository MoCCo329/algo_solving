T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[-1]*(M+2)] + [[-1] + list(map(int, input().split())) + [-1] for _ in range(N)] + [[-1]*(M+2)] # 사이드에 -1 붙이기

    di = [-1, -1, -1, 0, 0, 1, 1, 1]
    dj = [-1, 0, 1, -1, 1, -1, 0, 1]
    answer = 0

    for i in range(1, N+1):
        for j in range(1, M+1): # 주어진 지역을 조사
            h = arr[i][j]
            cnt = 0
            for k in range(8): # 지역 주변 8곳을 di dj를 통해 확인 
                if h > arr[i+di[k]][j+dj[k]] and arr[i+di[k]][j+dj[k]] != -1:
                    cnt += 1

            if cnt >= 4: # 4이상이면 답 1 추가
                answer += 1

    print(f'#{tc} {answer}')