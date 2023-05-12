# 디스크 컨트롤러.  2023-05-12


import heapq


def solution(jobs):
    
    jobs.sort()
    pq = []
    
    N = len(jobs)
    i = 0
    tot_turn_around = 0
    
    t = 0
    while i < N or pq:
        while i < N and jobs[i][0] <= t:
            heapq.heappush(pq, (jobs[i][1], jobs[i][0]))
            i += 1
        
        if not pq:
            t = jobs[i][0]
        else:
            b, s = heapq.heappop(pq)
            t += b
            tot_turn_around += t - s
    
    return tot_turn_around // N