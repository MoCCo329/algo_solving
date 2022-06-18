# 실패율 2019 KAKAO BLIND RECRUITMENT  2022-06-18


def solution(N, stages):
    counts = [0] * (N + 1)
    answer = [[i + 1, 0] for i in range(N)]
    
    for stage in stages:
        counts[stage - 1] += 1
    
    for i in range(N):
        temp = sum(counts[i:])
        if temp:
            answer[i][1] = counts[i] / sum(counts[i:])
        else:
            answer[i][1] = 0
    
    answer.sort(key=lambda x: (-x[1], x[0]))
    
    return [answer[i][0] for i in range(N)]