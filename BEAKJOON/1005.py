# 1005. ACM Craft  2023-01-10


T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    D_list = list(map(int, input().split()))
    out_deg = [[] for _ in range(N)]
    in_deg = [[] for _ in range(N)]
    for _ in range(K):
        o, i = map(lambda x: int(x) - 1, input().split())
        out_deg[o].append(i)
        in_deg[i].append(o)
    w = int(input()) - 1

    dp = []
    for i in range(N):
        if len(in_deg[i]) == 0:
            dp.append((D_list[i], i, -1))
    dp.sort()


    while dp:
        t, dist, src = dp.pop(0)

        if src != -1:
            in_deg[dist].remove(src)

        if len(in_deg[dist]) != 0: continue

        if dist == w:
            print(t)
            break

        if len(out_deg[dist]) > 0:
            for o in out_deg[dist]:
                dp.append((t + D_list[o], o, dist))
            dp.sort()