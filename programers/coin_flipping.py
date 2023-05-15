# 2차원 동전 뒤집기.  2023-05-15


def solution(beginning, target):
    global ans
    
    def dfs(k, bit, cnt):
        global ans
        
        if k == M:
            for i in range(N):
                before = beginning[i][0]
                if bit & 1: before = 1 if before == 0 else 0
                
                for j in range(1, M):
                    new = beginning[i][j]
                    if bit & (1 << j): new = 1 if new == 0 else 0
                    
                    if new != before: return
                    before = new
                
                if before == 1:
                    cnt += 1
            
            ans = min(ans, cnt)
            return

        dfs(k + 1, bit, cnt)
        dfs(k + 1, bit | (1 << k), cnt + 1)
    
    
    N = len(beginning)
    M = len(beginning[0])
    
    for i in range(N):
        for j in range(M):
            beginning[i][j] = beginning[i][j] ^ target[i][j]
    
    ans = N + M
    dfs(0, 0, 0)
    
    return -1 if ans == N + M else ans