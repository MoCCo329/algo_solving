# 코딩 테스트 연습.  2023-05-09


def solution(alp, cop, problems):
    problems.sort()
    N = len(problems)
    
    max_alp = max(alp, problems[-1][0])
    max_cop = cop
    for i in range(N):
        max_cop = max(max_cop, problems[i][1])
    
    dp = [[15000] * (max_cop + 1) for _ in range(max_alp + 1)]
    dp[alp][cop] = 0
    for i in range(alp, max_alp + 1):
        for j in range(cop, max_cop + 1):
            if i != max_alp:
                dp[i + 1][j] = min(dp[i][j] + 1, dp[i + 1][j])
            if j != max_cop:
                dp[i][j + 1] = min(dp[i][j] + 1, dp[i][j  + 1])
            
            for k in range(N):
                a, b, c, d, t = problems[k]
                if i < a: break
                
                if j >= b:
                    ii = min(max_alp, i + c)
                    jj = min(max_cop, j + d)
                    dp[ii][jj] = min(dp[i][j] + t, dp[ii][jj])
    
    return dp[max_alp][max_cop]