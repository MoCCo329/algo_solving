# 인사고과.  2023-04-16


def solution(scores):
    
    wanho = scores[0]
    ans, max_score = 1, 0
    
    scores.sort(key=lambda x: (-x[0], x[1]))
    
    for score in scores:
        if score[1] < max_score:
            if score[0] == wanho[0] and score[1] == wanho[1]:
                return -1
        else:
            max_score = max(max_score, score[1])
            if score[0] + score[1] > wanho[0] + wanho[1]:
                ans += 1
    
    return ans