# 징검다리 건너기.  2023-09-05


import heapq


def solution(stones, k):
    L = len(stones)
    counts = {}
    pq = []
    
    if L - 1 <= k:
        return min(stones)
    
    for i in range(k):
        if stones[i] not in counts:
            counts[stones[i]] = 1
            heapq.heappush(pq, -stones[i])
        else:
            counts[stones[i]] += 1
    
    ans = -pq[0]
    for i in range(k, L):
        if stones[i] not in counts or counts[stones[i]] == 0:
            counts[stones[i]] = 1
            heapq.heappush(pq, -stones[i])
        else:
            counts[stones[i]] += 1
        
        counts[stones[i - k]] -= 1
        if counts[stones[i - k]] == 0:
            while counts[-pq[0]] == 0:
                heapq.heappop(pq)
            ans = min(ans, -pq[0])
    
    return ans
