T = int(input())
for tc in range(1, T+1):
    s = input()

    answer = 0
    floor = [0] * 50000# 층별 레이저 수
    f = 0 # 층

    for i in range(len(s)):
        if s[i] == '(': # 층 증가
            f += 1
        else: # s[i] == ')'
            if s[i-1] == '(': # 레이저이면 해당 층까지 레이저 수 1씩 증가
                f -= 1
                for i in range(1, f+1):
                    floor[i] += 1
            else: # 레이저가 아니라 층이 사라지는 것이면 레이저 수 + 1 만큼 답 증가
                answer += floor[f] + 1
                floor[f] = 0
                f -= 1

    print(f'#{tc} {answer}')