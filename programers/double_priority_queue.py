# 이중우선순위큐.  2023-09-06


import heapq


def solution(operations):
    min_q = []
    max_q = []
    hash_count = {}
    
    for operation in operations:
        if operation == "D 1":
            while max_q and hash_count[-max_q[0]] == 0:
                heapq.heappop(max_q)
            if max_q:
                hash_count[-max_q[0]] -= 1
                heapq.heappop(max_q)
        elif operation == "D -1":
            while min_q and hash_count[min_q[0]] == 0:
                heapq.heappop(min_q)
            if min_q:
                hash_count[min_q[0]] -= 1
                heapq.heappop(min_q)
        else:
            n = int(operation[2:])
            if n not in hash_count:
                hash_count[n] = 0
            hash_count[n] += 1
            heapq.heappush(min_q, n)
            heapq.heappush(max_q, -n)
    
    while max_q and hash_count[-max_q[0]] == 0:
        heapq.heappop(max_q)
    while min_q and hash_count[min_q[0]] == 0:
        heapq.heappop(min_q)
    
    ans = [0, 0]
    if max_q:
        ans[0] = -max_q[0]
    if min_q:
        ans[1] = min_q[0]
    
    return ans
