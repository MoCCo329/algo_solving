# 14554. The Other Way  2023-08-30


from sys import stdin, maxsize
import heapq


input = stdin.readline


V, E, START, END = map(int, input().split())
adj_list = [dict() for _ in range(V + 1)]
d_list = [maxsize] * (V + 1)
ans = [0] * (V + 1)

for _ in range(E):
    a, b, w = map(int, input().split())
    if b in adj_list[a]:
        if w < adj_list[a][b][0]:
            adj_list[a][b] = [w, 1]
            adj_list[b][a] = [w, 1]
        elif w == adj_list[a][b][0]:
            adj_list[a][b][1] += 1
            adj_list[b][a][1] += 1
    else:
        adj_list[a][b] = [w, 1]
        adj_list[b][a] = [w, 1]

q = [(0, START)]
d_list[START] = 0
ans[START] = 1
while q:
    d, i = heapq.heappop(q)
    if d != d_list[i]:
        continue

    for j, (w, n) in adj_list[i].items():
        new_d = d + w
        if new_d == d_list[j]:
            ans[j] = (ans[j] + ans[i] * n) % 1000000009
        elif new_d < d_list[j]:
            d_list[j] = new_d
            ans[j] = (ans[i] * n) % 1000000009
            heapq.heappush(q, (new_d, j))

print(ans[END])
