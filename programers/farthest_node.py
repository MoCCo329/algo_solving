# 가장 먼 노드.  2023-09-07


import heapq, sys


INF = sys.maxsize

def solution(N, edges):
    adj_list = [[] for _ in range(N + 1)]
    for e in edges:
        adj_list[e[0]].append(e[1])
        adj_list[e[1]].append(e[0])
    
    pq = [(0, 1)]
    d_list = [INF] * (N + 1)
    d_list[1] = 0
    while pq:
        d, i = heapq.heappop(pq)
        if d_list[i] != d: continue
        
        for j in adj_list[i]:
            new_d = d + 1
            if new_d < d_list[j]:
                d_list[j] = new_d
                heapq.heappush(pq, (new_d, j))
    
    max_v = 0
    ans = 0
    for i in range(1, N + 1):
        if max_v < d_list[i]:
            max_v = d_list[i]
            ans = 1
        elif max_v == d_list[i]:
            ans += 1
    
    return ans
