# 13334. 철로  2023-01-21


import heapq


N = int(input())
p_list = []
low, high = 100000000, -100000000
for i in range(N):
    s, e = map(int, input().split())
    s, e = min(s, e), max(s, e)
    low = min(low, s)
    high = max(high, e)
    p_list.append((s, e))
D = int(input())

line = []
for i in range(N):
    s, e = p_list[i]
    if e - s > D: continue

    heapq.heappush(line, (-low - D + e, 1))
    heapq.heappush(line, (-low + s + 1, -1))

ans = 0
now = 0
while line:
    i, a = heapq.heappop(line)
    now += a
    ans = max(ans, now)

print(ans)