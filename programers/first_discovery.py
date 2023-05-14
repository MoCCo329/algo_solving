# 고고학 최초의 발견.  2023-05-14


def solution(clockHands):
    global ans
    
    
    def make_first_line(j, cnt):
        if j == N:
            test(cnt)
            return
        
        make_first_line(j + 1, cnt)
        for k in range(1, 4):
            if j - 1 >= 0:
                clockHands[0][j - 1] = (clockHands[0][j - 1] + k) % 4
            if j + 1 < N:
                clockHands[0][j + 1] = (clockHands[0][j + 1] + k) % 4
            clockHands[0][j] = (clockHands[0][j] + k) % 4
            clockHands[1][j] = (clockHands[1][j] + k) % 4
            
            make_first_line(j + 1, cnt + k)
            
            if j - 1 >= 0:
                clockHands[0][j - 1] = (clockHands[0][j - 1] - k) % 4
            if j + 1 < N:
                clockHands[0][j + 1] = (clockHands[0][j + 1] - k) % 4
            clockHands[0][j] = (clockHands[0][j] - k) % 4
            clockHands[1][j] = (clockHands[1][j] - k) % 4
    
    
    def test(cnt):
        global ans
        
        temp = [[0] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                temp[i][j] = clockHands[i][j]
        
        for i in range(1, N):
            if cnt >= ans: return
        
            for j in range(N):
                if temp[i - 1][j] != 0:
                    k = 4 - temp[i - 1][j]
                    cnt += k
                    if j - 1 >= 0:
                        temp[i][j - 1] = (temp[i][j - 1] + k) % 4
                    if j + 1 < N:
                        temp[i][j + 1] = (temp[i][j + 1] + k) % 4
                    temp[i][j] = (temp[i][j] + k) % 4
                    if i + 1 < N:
                        temp[i + 1][j] = (temp[i + 1][j] + k) % 4
        
        for j in range(N):
            if temp[N - 1][j] != 0:
                return
        
        ans = min(ans, cnt)

    
    N = len(clockHands)
    ans = 4 * N * N
    make_first_line(0, 0)
    
    return ans
    