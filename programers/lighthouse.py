# 등대.  2023-05-16


import sys
sys.setrecursionlimit(100000)


def solution(n, lighthouse):

    def dfs(i):
        vis[i] = 1
        
        for j in adj_list[i]:
            if vis[j] == 1: continue
            dfs(j)
            dp[i][1] += min(dp[j])
            dp[i][0] += dp[j][1]
    
    
    adj_list = [[] for _ in range(n + 1)]
    for l in lighthouse:
        adj_list[l[0]].append(l[1])
        adj_list[l[1]].append(l[0])
    
    dp = [[0, 1] for _ in range(n + 1)]
    vis = [0] * (n + 1)
    dfs(1)
    
    return min(dp[1])