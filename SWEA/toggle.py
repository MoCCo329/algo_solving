T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0 # 전체 토글 횟수

    for k in range(1, M+1):
        if M % k == 0: # k가 M의 약수인경우 전체 토글
            cnt += 1
        else:
            for i in range(N):
                for j in range(N):
                    if (i+j+2)%k == 0: # 배열이 1부터 시작이니까 2를 더해준다.
                        if arr[i][j] == 1:
                            arr[i][j] = 0
                        else:
                            arr[i][j] = 1

    answer = 0
    for i in range(N):
        for j in range(N):
            if cnt%2==0 and arr[i][j]: # 전체 토글 횟수가 짝수면 1인칸을 센다
                answer += 1
            elif cnt%2==1 and not arr[i][j]: # 홀수면 0인칸을 센다
                answer += 1

    print(f'#{tc} {answer}')