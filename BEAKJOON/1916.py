# 1916. 최소비용 구하기  2022-09-09


import heapq


N = int(input())
M = int(input())

adj_list = [[] for _ in range(M)]
for _ in range(M):
    a, b, w = map(int, input().split())
    adj_list[a - 1].append((b - 1, w))

start, end = map(int, input().split())

hq = []
heapq.heappush(hq, (0, start - 1))
D = [-1] * N
D[start - 1] = 0

while hq:
    min_d, min_idx = heapq.heappop(hq)
    if D[min_idx] != min_d: continue
    if min_idx == end - 1: break

    for next_idx, next_d in adj_list[min_idx]:
        new_d = min_d + next_d

        if D[next_idx] == -1 or D[next_idx] > new_d:
            D[next_idx] = new_d
            heapq.heappush(hq, (new_d, next_idx))

print(D[end - 1])