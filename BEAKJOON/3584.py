# 3584. 가장 가까운 공통 조상  2023-01-27


from collections import deque


def get_level_bfs():
    idx = -1
    for i in range(N):
        if i == parents[i]:
            idx = i

    q = deque()
    q.append((idx, 0))

    while q:
        i, d = q.popleft()
        level[i] = d
        for j in adj_list[i]:
            q.append((j, d + 1))


def LCA(i, j):
    while level[i] != level[j]:
        if level[i] > level[j]:
            i = parents[i]
        else:
            j = parents[j]

    while i != j:
        i = parents[i]
        j = parents[j]

    return i


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    adj_list = [[] for _ in range(N)]
    parents = [i for i in range(N)]
    level = [0] * N
    for _ in range(N - 1):
        p, c = map(lambda x: int(x) - 1, input().split())
        adj_list[p].append(c)
        parents[c] = p

    i, j = map(lambda x: int(x) - 1, input().split())
    get_level_dfs()
    print(LCA(i, j) + 1)