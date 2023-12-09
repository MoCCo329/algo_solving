# 배달.  2023-12-09


import heapq

INF = 500001

def solution(N, roads, K):
    adj_list = [[] for _ in range(N + 1)]
    
    for road in roads:
        adj_list[road[0]].append((road[1], road[2]))
        adj_list[road[1]].append((road[0], road[2]))
    
    D = [INF] * (N + 1)
    vis = [False] * (N + 1)
    pq = [(0, 1)]
    D[1] = 0
    ans = 0
    while pq:
        d, i = heapq.heappop(pq)
        if vis[i]: continue
        if K < d:
            break
        
        vis[i] = True
        ans += 1
        for j, nd in adj_list[i]:
            if D[j] <= d + nd: continue
            D[j] = d + nd
            heapq.heappush(pq, (d + nd, j))
    
    return ans