# 정수 삼각형.  2023-09-09


def solution(triangle):
    
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            v1, v2 = 0, 0
            if j != len(triangle[i]) - 1: v1 = triangle[i - 1][j]
            if 0 < j: v2 = triangle[i - 1][j - 1]
            
            triangle[i][j] = triangle[i][j] + max(v1, v2)
    
    return max(triangle[-1])
