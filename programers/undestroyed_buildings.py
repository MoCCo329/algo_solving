# 파괴되지 않은 건물.  2023-05-11


def solution(board, skills):
    N = len(board)
    M = len(board[0])
    
    maps = [[0] * M for _ in range(N)]
    
    for t, i1, j1, i2, j2, d in skills:
        if t == 1: d = -d
        
        maps[i1][j1] += d
        if j2 + 1 < M:
            maps[i1][j2 + 1] -= d
        if i2 + 1 < N:
            maps[i2 + 1][j1] -= d
        if i2 + 1 < N and j2 + 1 < M:
            maps[i2 + 1][j2 + 1] += d
    
    for i in range(N):
        for j in range(1, M):
            maps[i][j] += maps[i][j - 1]
    for j in range(M):
        for i in range(1, N):
            maps[i][j] += maps[i - 1][j]
    
    ans = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] + maps[i][j] > 0:
                ans += 1
    
    return ans