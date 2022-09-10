# 1967 트리의 지름.  2022-09-10


def get_dia(i):
    q = [(0, i)]
    D = [-1] * (N + 1)
    D[i] = 0

    while q:
        d, j = q.pop(0)
        if D[j] < d: continue

        for k, w in adj_list[j]:
            if D[k] == -1 or D[k] > d + w:
                D[k] = d + w
                q.append((D[k], k))

    max_v = max(D)
    return D.index(max_v), max_v


N = int(input())
adj_list = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b, w = map(int, input().split())
    adj_list[a].append((b, w))
    adj_list[b].append((a, w))

print(get_dia(get_dia(1)[0])[1])