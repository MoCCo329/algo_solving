# 2696. 중앙값 구하기  2023-02-27


import heapq


T = int(input())
for tc in range(1, T + 1):
    M = int(input())
    lower = []
    higher = []
    ite = iter(map(int, input().split()))
    mid = next(ite)
    cnt = 1
    print_cnt = 1

    print(M // 2 + 1)
    print(mid, end=" ")
    for i in range(M // 2):
        a = next(ite)
        cnt += 1
        if cnt == 10:
            ite = iter(map(int, input().split()))
            cnt = 0
        b = next(ite)
        cnt += 1

        if a < b: a, b = b, a

        if mid > a:
            heapq.heappush(lower, -a)
            heapq.heappush(lower, -b)
            heapq.heappush(higher, mid)
            mid = -heapq.heappop(lower)
        elif mid < b:
            heapq.heappush(higher, a)
            heapq.heappush(higher, b)
            heapq.heappush(lower, -mid)
            mid = heapq.heappop(higher)
        else:
            heapq.heappush(higher, a)
            heapq.heappush(lower, -b)

        print(mid, end=" ")
        print_cnt += 1
        if print_cnt == 10:
            print()
            print_cnt = 0

    if print_cnt > 0:
        print()
