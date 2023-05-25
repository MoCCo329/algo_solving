# 5022. 연결  2023-05-25


from collections import deque


x = lambda : list(map(int, input().split()))
N, M = map(int, input().split())
A1 = x()
A2 = x()
B1 = x()
B2 = x()

ans = (N + 1) * (M + 1)
temp = [(A1, A2), (B1, B2)]
for _ in range(2):
    s, e = temp[0]
    vis = [[0] * (M + 1) for _ in range(N + 1)]
    q = deque()
    q.append((*s, set()))
    vis[s[0]][s[1]] = 1
    vis[temp[1][0][0]][temp[1][0][1]] = 1
    vis[temp[1][1][0]][temp[1][1][1]] = 1
    while q:
        i, j, path = q.popleft()
        path.add((i, j))
        if i == e[0] and j == e[1]:
            ns, ne = temp[1]
            nvis = [[0] * (M + 19) for _ in range(N + 1)]
            nq = deque()
            nq.append((*ns, 0))
            nvis[ns[0]][ns[1]] = 1
            while nq:
                ii, jj, cnt = nq.popleft()
                if ii == ne[0] and jj == ne[1]:
                    ans = min(ans, len(path) + cnt - 1)
                    break

                for di, dj in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    ni, nj = ii + di, jj + dj
                    if not (0 <= ni <= N) or not (0 <= nj <= M): continue
                    if nvis[ni][nj] == 1 or (ni, nj) in path: continue
                    nvis[ni][nj] = 1
                    nq.append((ni, nj, cnt + 1))
            break

        for di, dj in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            ni, nj = i + di, j + dj
            if not (0 <= ni <= N) or not (0 <= nj <= M): continue
            if vis[ni][nj] == 1: continue
            vis[ni][nj] = 1
            q.append((ni, nj, path.copy()))

    temp[0], temp[1] = temp[1], temp[0]

if ans == (N + 1) * (M + 1):
    print("IMPOSSIBLE")
else:
    print(ans)