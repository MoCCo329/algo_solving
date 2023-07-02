# 4196. 도미노  2023-07-02


import sys
sys.setrecursionlimit(100001)
input = sys.stdin.readline


def dfs(i):
    global ids, g_id

    ids += 1
    d[i] = ids
    p = ids
    stack.append(i)

    for j in adj_list[i]:
        if d[j] == 0:
            p = min(p, dfs(j))
        elif not is_finished[j]:
            p = min(p, d[j])

    if d[i] == p:
        while stack:
            j = stack.pop()
            is_finished[j] = True
            group[j] = g_id
            if j == i: break
        g_id += 1

    return p


T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    adj_list = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(lambda x: int(x) - 1, input().split())
        adj_list[a].append(b)

    is_finished = [False] * N
    d = [0] * N
    ids = 0
    group = [0] * N
    g_id = 1
    stack = []

    for i in range(N):
        if d[i] == 0:
            dfs(i)

    in_degree = [0] * g_id
    for i in range(N):
        for j in adj_list[i]:
            if group[i] != group[j]:
                in_degree[group[j]] += 1

    ans = 0
    for i in range(1, g_id):
        if in_degree[i] == 0:
            ans += 1

    print(1 if ans == 0 else ans)