T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    L = [i for i in range(1, 13)]

    answer = 0
    for i in range(1<<12): # 가능한 합집합의 수 생성
        sum = 0
        cnt = 0
        for j in range(12): # 12개의 스위치
            if i & (1<<j): # 켜진 스위치가 있으면 cnt += 1, sum에 더하기
                cnt += 1
                sum += L[j]
        if cnt == N and sum == K: #cnt가 주어진 N과 같고, sum이 K와 같으면 answer += 1
            answer += 1

    print(f'#{tc} {answer}')