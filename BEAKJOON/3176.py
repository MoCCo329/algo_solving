# 3176. 도로 네트워크  2023-03-04


from collections import deque
import sys
input = sys.stdin.readline


def LCA(a, b):
    if lank[a] < lank[b]:
        a, b = b, a

    maxV = 0
    minV = 1000001

    for k in range(16, -1, -1):
        if lank[a] - lank[b] >= (1 << k):
            maxV = max(maxV, parents[a][k][1])
            minV = min(minV, parents[a][k][2])
            a = parents[a][k][0]

    if a == b: return minV, maxV

    for k in range(16, -1, -1):
        if parents[a][k][0] != parents[b][k][0]:
            maxV = max(maxV, parents[a][k][1], parents[b][k][1])
            minV = min(minV, parents[a][k][2], parents[b][k][2])
            a = parents[a][k][0]
            b = parents[b][k][0]
    maxV = max(maxV, parents[a][0][1], parents[b][0][1])
    minV = min(minV, parents[a][0][2], parents[b][0][2])

    return minV, maxV


N = int(input())
adj_list = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b, d = map(int, input().split())
    adj_list[a].append((b, d))
    adj_list[b].append((a, d))
M = int(input())

parents = [[(0, 0, 1000001) for _ in range(17)] for _ in range(N + 1)]
parents[1][0] = (1, 0, 1000001)

lank = [-1] * (N + 1)
lank[1] = 1
q = deque()
q.append((1, 1))
while q:
    now = q.popleft()
    for next_node in adj_list[now[0]]:
        if lank[next_node[0]] != -1: continue
        lank[next_node[0]] = now[1] + 1
        parents[next_node[0]][0] = (now[0], next_node[1], next_node[1])
        q.append((next_node[0], now[1] + 1))

for k in range(1, 17):
    for i in range(1, N + 1):
        temp1 = parents[i][k - 1]
        temp2 = parents[temp1[0]][k - 1]
        parents[i][k] = (temp2[0], max(temp1[1], temp2[1]), min(temp1[2], temp2[2]))

for _ in range(M):
    a, b = map(int, input().split())
    print(*LCA(a, b))