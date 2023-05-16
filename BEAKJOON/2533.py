# 2533. 사회망 서비스(SNS)  2023-05-16


import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def dfs(i):

    vis[i] = 1
    temp = [0, 1]

    for j in adj_list[i]:
        if vis[j] == 1: continue
        c_temp = dfs(j)
        temp[0] += c_temp[1]
        temp[1] += min(c_temp)

    return temp


N = int(input())
adj_list = [[] for _ in range(N + 1)]
vis = [0] * (N + 1)

for _ in range(N - 1):
    a, b = map(int, input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

print(min(dfs(1)))