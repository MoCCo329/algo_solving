# 11400. 단절선  2023-04-25


import sys
input = lambda: map(int, sys.stdin.readline().split())
sys.setrecursionlimit(100000)

def dfs(i, parent):
    global count

    count += 1
    vis[i] = count
    min_v = count

    for j in adj_list[i]:
        if j == parent: continue

        if vis[j] == 0:
            temp_min_v = dfs(j, i)
            if temp_min_v > vis[i]: edges.append((min(i, j), max(i, j)))

            min_v = min(min_v, temp_min_v)

        else:
            min_v = min(min_v, vis[j])

    return min_v


V, E = input()
adj_list = [[] for _ in range(V + 1)]
for _ in range(E):
    a, b = input()
    adj_list[a].append(b)
    adj_list[b].append(a)

edges = []
vis = [0] * (V + 1)
count = 0
dfs(1, 0)

edges.sort()
print(len(edges))
for a, b in edges:
    print(a, b)