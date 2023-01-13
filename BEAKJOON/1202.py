# 1202. 보석 도둑  2023-01-13


import heapq


N, K = map(int, input().split())
items = []
for _ in range(N):
    heapq.heappush(items, tuple(map(int, input().split())))
bags = [int(input()) for _ in range(K)]
bags.sort()

ans = 0
next_items = []
for i in range(K):
    while items and items[0][0] <= bags[i]:
        heapq.heappush(next_items, -heapq.heappop(items)[1])

    if next_items:
        ans += -heapq.heappop(next_items)

print(ans)