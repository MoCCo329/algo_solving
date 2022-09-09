# 1167 트리의 지름.  2022-09-09


def find_dia(i):
    v = [-1] * V
    v[i] = 0
    q = [i]

    while q:
        j = q.pop(0)
        for k, w in adj_list[j]:
            if v[k] == -1:
                v[k] = w + v[j]
                q.append(k)

    return [max(v), v.index(max(v))]


V = int(input())
adj_list = [[] for _ in range(V)]
for _ in range(V):
    a, *b_list = map(int, input().split())
    for i in range(0, len(b_list) - 1, 2):
        adj_list[a - 1].append((b_list[i] - 1, b_list[i + 1]))

print(find_dia(find_dia(0)[1])[0])