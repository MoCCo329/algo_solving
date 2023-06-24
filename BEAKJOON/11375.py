# 11375. 열혈강호  2023-06-24


def dfs(i):
    for w in poss[i]:
        if vis[w]: continue
        vis[w] = True
        if occ[w] == 0 or dfs(occ[w]):
            occ[w] = i
            return True
    return False


N, M = map(int, input().split())
poss = [[]]
for _ in range(N):
    n, *works = map(int, input().split())
    poss.append(works)

vis = [False] * (M + 1)
occ = [0] * (M + 1)

ans = 0
for i in range(1, N + 1):
    for k in range(1, M + 1):
        vis[k] = False
    if dfs(i):
        ans += 1

print(ans)