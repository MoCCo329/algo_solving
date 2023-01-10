# 1005. ACM Craft  2023-01-10


import heapq

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    D_list = list(map(int, input().split()))
    out_deg = [[] for _ in range(N)]
    in_deg = [0 for _ in range(N)]
    for _ in range(K):
        o, i = map(lambda x: int(x) - 1, input().split())
        out_deg[o].append(i)
        in_deg[i] += 1
    w = int(input()) - 1

    hq = []
    for i in range(N):
        if in_deg[i] == 0:
            heapq.heappush(hq, (D_list[i], i))

    while hq:
        t, dist = heapq.heappop(hq)

        in_deg[dist] -= 1

        if in_deg[dist] > 0: continue

        if dist == w:
            print(t)
            break

        for o in out_deg[dist]:
            heapq.heappush(hq, (t + D_list[o], o))