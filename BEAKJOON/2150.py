# 2150. Stringly Connected Component  2023-06-03


import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)


def dfs(i):
    global ids

    p = ids
    ids += 1
    d[i] = p
    stack.append(i)

    for j in adj_list[i]:
        if d[j] == 0:
            p = min(p, dfs(j))
        elif not is_finished[j]:
            p = min(p, d[j])

    if p == d[i]:
        scc = []
        while True:
            scc.append(stack.pop())
            is_finished[scc[-1]] = True
            if scc[-1] == i: break
        scc.sort()
        SCC.append(scc)

    return p


V, E = map(int, input().split())
adj_list = [[] for _ in range(V + 1)]
for _ in range(E):
    a, b = map(int, input().split())
    adj_list[a].append(b)

d = [0] * (V + 1)
is_finished = [False] * (V + 1)
stack = []
SCC = []
ids = 1

for i in range(1, V + 1):
    if d[i] == 0:
        dfs(i)

print(len(SCC))
SCC.sort(key=lambda x: x[0])
for scc in SCC:
    print(*scc, -1)