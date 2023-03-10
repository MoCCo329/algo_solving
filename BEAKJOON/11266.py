# 11266. 단절점  2023-03-11


import sys
sys.setrecursionlimit(10001)
input = sys.stdin.readline


def dfs(node, is_root):
    global counter

    counter += 1
    discovered[node] = counter
    min_count = discovered[node]

    child = 0
    for next_node in adj_list[node]:
        if discovered[next_node]:
            min_count = min(min_count, discovered[next_node])
        else:
            child += 1
            low_count = dfs(next_node, False)
            if not is_root and low_count >= discovered[node]:
                is_cut_vertex[node] = True
            min_count = min(min_count, low_count)

    if is_root:
        is_cut_vertex[node] = child >= 2
    return min_count


V, E = map(int, input().split())
adj_list = [[] for _ in range(V + 1)]
for _ in range(E):
    a, b = map(int, input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

is_cut_vertex = [False] * (V + 1)
discovered = [0] * (V + 1)
counter = 0

for i in range(1, V + 1):
    if discovered[i] == 0:
        dfs(i, True)

ans = 0
for i in range(1, V + 1):
    if is_cut_vertex[i]:
        ans += 1
print(ans)

for i in range(1, V + 1):
    if is_cut_vertex[i]:
        print(i, end=" ")