# 등산 코스 정하기.  2023-04-20


import heapq


def solution(N, paths, gates, summits):
    summits.sort()
    INF = 500000000000
    
    orders = [0] * (N + 1)
    for gate in gates:
        orders[gate] = 1
    for summit in summits:
        orders[summit] = 2
        
    adj_list = [[] for _ in range(N + 1)]
    for path in paths:
        adj_list[path[0]].append((path[1], path[2]))
        adj_list[path[1]].append((path[0], path[2]))
    
    ans = [0, INF]
    for summit in summits:
        dist = [INF] * (N + 1)
        dist[summit] = 0
        vis = [0] * (N + 1)
        pq = [(0, summit)]
        
        end = 0
        while pq:
            d, i = heapq.heappop(pq)
            if dist[i] != d: continue
            if orders[i] == 1:
                end = i
                break
            
            vis[i] = 1
            
            for j, nd in adj_list[i]:
                if orders[j] == 2 or vis[j] == 1: continue
                new_dist = max(d, nd)
                if dist[j] < new_dist: continue
                
                dist[j] = new_dist
                heapq.heappush(pq, (new_dist, j))
        
        temp_ans = [summit, dist[end]]
        if ans[1] > temp_ans[1]:
            ans = temp_ans
    
    return ans