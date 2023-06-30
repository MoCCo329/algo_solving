# 1506. 경찰서  2023-06-30


def dfs(i):
    global ids, ans

    d[i] = ids
    p = ids
    ids += 1
    stack.append(i)

    for j in range(N):
        if adj_matrix[i][j] == 0: continue
        if d[j] == 0:
            p = min(p, dfs(j))
        elif not is_finished[j]:
            p = min(p, d[j])

    if p == d[i]:
        min_v = 1000000
        while True:
            temp = stack.pop()
            is_finished[temp] = True
            min_v = min(min_v, costs[temp])
            if temp == i: break
        ans += min_v

    return p


N = int(input())
costs = list(map(int, input().split()))
adj_matrix = [list(map(int, input())) for _ in range(N)]
ids = 1
d = [0] * N
is_finished = [False] * N
stack = []
ans = 0

for i in range(N):
    if d[i] == 0:
        dfs(i)

print(ans)