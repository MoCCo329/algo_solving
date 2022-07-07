# 14466. 소가 길을 건너간 이유6 2022-07-07


N, K, R = map(int, input().split())
gates = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(R):
    i1, j1, i2, j2 = map(int, input().split())
    i1, j1, i2, j2 = i1 - 1, j1 - 1, i2 - 1, j2 - 1
    gates[i1][j1].append((i2 - i1, j2 - j1))
    gates[i2][j2].append((i1 - i2, j1 - j2))

cows = []
for _ in range(K):
    i, j = map(int, input().split())
    cows.append((i, j))

v = [[0] * N for _ in range(N)]
cnt = 0
for i in range(N):
    for j in range(N):
        if v[i][j]: continue

        cnt += 1
        v[i][j] = cnt
        q = [(i, j)]

        while q:
            ii, jj = q.pop(0)
            for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                if (di, dj) in gates[ii][jj]:
                    continue
                ni, nj = ii + di, jj + dj
                if 0 <= ni < N and 0 <= nj < N and v[ni][nj] == 0:
                    q.append((ni, nj))
                    v[ni][nj] = cnt

counts = [0] * (cnt + 1)
for i, j in cows:
    counts[v[i - 1][j - 1]] += 1

ans = 0
for i in range(1, cnt + 1):
    if counts[i] == 0: continue
    for j in range(i + 1, cnt + 1):
        if counts[j]:
            ans += counts[i] * counts[j]
print(ans)