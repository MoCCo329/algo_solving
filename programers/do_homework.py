# 과제 진행하기.  2023-08-23


import heapq


def convert_time(t):
    return int(t[:2]) * 60 + int(t[3:5])


def solution(plans):
    ans = []
    pq = []
    
    for plan in plans:
        heapq.heappush(pq, (convert_time(plan[1]), int(plan[2]), plan[0]))
    heapq.heappush(pq, (100000000, 0, ""))
    
    stack = [heapq.heappop(pq)]
    time = stack[-1][0]
    while pq:
        plan = heapq.heappop(pq);

        while stack and time < plan[0]:
            now = stack.pop()
            if time + now[1] <= plan[0]:
                ans.append(now[2])
                time += now[1]
            else:
                stack.append((now[0], now[1] - (plan[0] - time), now[2]))
                break

        stack.append((plan[0], plan[1], plan[2]))
        time = plan[0]

    return ans