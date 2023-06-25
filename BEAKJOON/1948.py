# 1948. 임계경로  2023-06-25


from collections import deque
import sys
input = sys.stdin.readline


N = int(input())
M = int(input())
adj_list = [[] for _ in range(N + 1)]
rev_adj_list = [[] for _ in range(N + 1)]
in_order = [0] * (N + 1)
for _ in range(M):
    a, b, t = map(int, input().split())
    adj_list[a].append((b, t))
    rev_adj_list[b].append((a, t))
    in_order[b] += 1

start, end = map(int, input().split())
times = [0] * (N + 1)
q = deque()
q.append(start)
while q:
    i = q.popleft()
    for j, t in adj_list[i]:
        times[j] = max(times[j], times[i] + t)
        in_order[j] -= 1
        if in_order[j] == 0:
            q.append(j)

ans = 0
q = deque()
q.append(end)
while q:
    i = q.popleft()
    while rev_adj_list[i]:
        j, t = rev_adj_list[i].pop()
        if times[j] != times[i] - t: continue
        ans += 1
        q.append(j)

print(times[end])
print(ans)