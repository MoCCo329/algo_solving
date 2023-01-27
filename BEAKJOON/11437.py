# 11437. LCA  2023-01-27


import sys
from collections import deque


def get_level_bfs():
    v = [0] * N
    v[0] = 1

    q = deque()
    q.append((0, 0))

    while q:
        i, d = q.popleft()
        for j in adj_list[i]:
            if v[j]: continue
            v[j] = 1
            parents[j][0] = i
            level[j] = d + 1
            q.append((j, d + 1))


def LCA(i, j):
    if level[i] > level[j]:
        i, j = j, i

    for k in range(16, -1, -1):
        if level[j] - level[i] >= (1 << k):
            j = parents[j][k]

    if i == j: return i

    x, y = i, j
    if (i, j) in history: return history[(i, j)]

    for k in range(16, -1, -1):
        if parents[i][k] != parents[j][k]:
            i = parents[i][k]
            j = parents[j][k]

    history[(x, y)] = parents[i][0]
    return parents[i][0]


input = sys.stdin.readline
N = int(input())
adj_list = [[] for _ in range(N)]
parents = [[0] * 17 for _ in range(N)]
level = [0] * N
history = dict()

for _ in range(N - 1):
    p, c = map(lambda x: int(x) - 1, input().split())
    adj_list[p].append(c)
    adj_list[c].append(p)

get_level_bfs()

for i in range(1, 17):
    for j in range(N):
        parents[j][i] = parents[parents[j][i - 1]][i - 1]

for _ in range(int(input())):
    i, j = map(lambda x: int(x) - 1, input().split())
    print(LCA(i, j) + 1)