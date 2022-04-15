# 14502. 연구소 2022-04-15


def pen():
    V = [[0] * M for _ in range(N)]
    q = [_ for _ in viruses]
    while q:
        i, j = q.pop(0)
        V[i][j] = 1
        for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] != 1 and V[ni][nj] == 0:
                q.append([ni, nj])
                V[ni][nj] = 1

    return N * M - sum([sum(line) for line in V]) - wall_cnt


def blocking(k, cnt):
    global ans

    if cnt == 3:
        for i in B:
            arr[i // M][i % M] = 1

        temp = pen()
        if ans < temp:
            ans = temp

        for i in B:
            arr[i // M][i % M] = 0

    else:
        if N * M - k < 3 - cnt:
            return
        else:
            if arr[k // M][k % M] == 0:
                B[cnt] = k
                blocking(k + 1, cnt + 1)
            blocking(k + 1, cnt)


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
viruses = []
wall_cnt = 3
B = [0] * 3
ans = 0

for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            viruses.append([i, j])
        elif arr[i][j] == 1:
            wall_cnt += 1

blocking(0, 0)
print(ans)