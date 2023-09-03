# 단속카메라.  2023-09-03


def solution(routes):
    N = len(routes)
    routes.sort(key=lambda x: x[1])
    ans = 0
    last = -30001
    
    for route in routes:
        if route[0] <= last:
            continue
        ans += 1
        last = route[1]
    
    return ans
