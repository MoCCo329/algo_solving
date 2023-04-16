# 1,2,3 떨어트리기.  2023-04-17


from collections import deque


def solution(edges, target):
    N = 0
    edges.sort(key = lambda x: x[1])
    N = edges[-1][1]
    
    adj_list = [deque() for _ in range(N + 1)]
    for edge in edges:
        adj_list[edge[0]].append(edge[1])
    
    K = 0
    for t in target:
        if t != 0: K += 1
    
    orders = []
    counts = [0] * (N + 1)
    vis = [0] * (N + 1)
    k = K
    cnt = 0
    while True:
        cnt += 1
        idx = 1
        while True:
            if len(adj_list[idx]) == 0:
                break
            
            next_idx = adj_list[idx].popleft()
            adj_list[idx].append(next_idx)
            idx = next_idx
        
        counts[idx] += 1
        orders.append(idx)
        
        # break 판단
        if counts[idx] <= target[idx - 1] <= counts[idx] * 3:
            if vis[idx] == 0:
                vis[idx] = 1
                k -= 1
                if k == 0:
                    break
        else:
            if vis[idx] == 1:
                return [-1]
    
    ans = []
    for idx in orders:
        counts[idx] -= 1
        c = counts[idx]
        
        if c <= target[idx - 1] - 1 <= c * 3:
            target[idx - 1] -= 1
            ans.append(1)
        elif c <= target[idx - 1] - 2 <= c * 3:
            target[idx - 1] -= 2
            ans.append(2)
        else:
            target[idx - 1] -= 3
            ans.append(3)
    
    return ans