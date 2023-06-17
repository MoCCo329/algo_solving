# 1199. 오일러 회로  2023-06-18


import sys
input = sys.stdin.readline


N = int(input())
adj_matrix = [list(map(int, input().split())) for _ in range(N)]
adj_list = [[] for _ in range(N)]
tot = 0
for i in range(N):
    cnt = 0
    for j in range(N):
        if adj_matrix[i][j] == 0: continue
        cnt += adj_matrix[i][j]
        adj_list[i].extend([j] * adj_matrix[i][j])
    if cnt % 2 == 1:
        print(-1)
        exit(0)
    tot += cnt

stack = []
dfs_stack = [0]
while dfs_stack:
    i = dfs_stack[-1]
    mark = 0
    while adj_list[i]:
        j = adj_list[i].pop()
        if adj_matrix[i][j] == 0: continue
        adj_matrix[i][j] -= 1
        adj_matrix[j][i] -= 1
        dfs_stack.append(j)
        tot -= 2
        mark = 1
        break
    if mark == 1:
        continue
    dfs_stack.pop()
    stack.append(i + 1)

if tot != 0:
    print(-1)
else:
    print(*stack)