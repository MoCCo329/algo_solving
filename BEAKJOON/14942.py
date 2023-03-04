# 14942. 개미  2023-03-05


import sys
from collections import deque
input = sys.stdin.readline


def goTop(i, e):
    for j in range(k - 1, -1, -1):
        if i == 1: return 1

        # if

        if parents[i][j][1] <= e:
            e -= parents[i][j][1]
            i = parents[i][j][0]

    return i


N = int(input())
adj_list = [[] for _ in range(N + 1)]
energy = [int(input()) for _ in range(N)]
for _ in range(N - 1):
    a, b, d = map(int, input().split())
    adj_list[a].append((b, d))
    adj_list[b].append((a, d))

k = 1
while (1 << k) < N: k += 1
parents = [[(0, 0) for _ in range(k)] for _ in range(N + 1)]

parents[1][0] = (1, 0)
q = deque()
q.append(1)
while q:
    now = q.popleft()
    for next_node, d in adj_list[now]:
        if parents[next_node][0][0] != 0: continue
        parents[next_node][0] = (now, d)
        q.append(next_node)

for j in range(1, k):
    for i in range(1, N + 1):
        temp1 = parents[i][j - 1]
        temp2 = parents[temp1[0]][j - 1]
        parents[i][j] = (temp2[0], temp2[1] + temp1[1])

for i in range(N):
    print(goTop(i + 1, energy[i]))