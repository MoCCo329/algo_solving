# 요격 시스템.  2023-04-24


def solution(targets):
    targets.sort(key=lambda x: (x[1], x[0]))
    N = len(targets)
    
    ans = 1
    i = 0
    before = [-1, 100000001]
    while i < N:
        if before[1] > targets[i][0]:
            before = [max(before[0], targets[i][0]), min(before[1], targets[i][1])]
        else:
            ans += 1
            before = targets[i]
        
        i += 1
    
    return ans