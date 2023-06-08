# 13975. 파일 합치기 3  2023-06-08


import sys
import heapq
input = sys.stdin.readline


T = int(input())
for tc in range(T):
    N = int(input())
    iterator = map(int, input().split())
    pq = []
    for _ in range(N):
        heapq.heappush(pq, next(iterator))

    ans = 0
    for _ in range(N - 1):
        a, b = heapq.heappop(pq), heapq.heappop(pq)
        ans += a + b
        heapq.heappush(pq, a + b)

    print(ans)