# 두 원 사이의 정수 쌍.  2023-04-19


def solution(r1, r2):
    outer = 0
    for n in range(1, r2 + 1):
        outer += int((r2 ** 2 - n ** 2) ** 0.5) + 1
    outer = outer * 4 + 1
    
    inner = 0
    for n in range(1, r1 + 1):
        temp = int((r1 ** 2 - n ** 2) ** 0.5)
        if temp ** 2 == (r1 ** 2 - n ** 2):
            inner += temp
        else:
            inner += temp + 1
    inner = inner * 4 + 1
    
    return outer - inner