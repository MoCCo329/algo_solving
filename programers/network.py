# 네트워크.  2023-09-03


def find(i):
    global uf
    
    if uf[i] == i:
        return i
    
    uf[i] = find(uf[i])
    return uf[i]


def union(x, y):
    global uf
    
    X = find(x)
    Y = find(y)
    
    uf[X] = Y


def solution(N, computers):
    global uf
    
    uf = [i for i in range(N)]
    
    for i in range(1, N):
        for j in range(i):
            if computers[i][j] == 1:
                union(i, j)
    
    counts = [False] * N
    ans = 0
    for i in range(N):
        idx = find(i)
        if not counts[idx]:
            ans += 1
        counts[idx] = True
    
    return ans
