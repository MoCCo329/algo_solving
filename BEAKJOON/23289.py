# 23289. 온풍기 안녕!  2022-10-16


def heat(i, j, d, n):
    if n >= 5:
        return

    arr[i][j] += 5 - n
    v[i][j] = 1

    di, dj = d_list[d]

    if 0 <= i + di < N and 0 <= j + dj < M and not v[i + di][j + dj] and not (di, dj) in walls[i][j]:
        heat(i + di, j + dj, d, n + 1)
    if not dj:
        for dj in [-1, 1]:
            if 0 <= i + di < N and 0 <= j + dj < M and not v[i + di][j + dj] and not (0, dj) in walls[i][j] and not (di, 0) in walls[i][j + dj]:
                heat(i + di, j + dj, d, n + 1)
    elif not di:
        for di in [-1, 1]:
            if 0 <= i + di < N and 0 <= j + dj < M and not v[i + di][j + dj] and not (di, 0) in walls[i][j] and not (0, dj) in walls[i + di][j]:
                heat(i + di, j + dj, d, n + 1)


d_list = [(0, 1), (0, -1), (-1, 0), (1, 0)]
N, M, K = map(int, input().split())
arr = [[0] * M for _ in range(N)]
airs = []
sensors = []
for i in range(N):
    line = list(map(int, input().split()))
    for j in range(M):
        if line[j] == 5:
            sensors.append((i, j))
        elif 0 < line[j]:
            airs.append((i, j, line[j] - 1))

walls = [[[] for _ in range(M)] for _ in range(N)]
for _ in range(int(input())):
    i, j, d = map(int, input().split())
    if d == 0:
        walls[i - 1][j - 1].append((-1, 0))
        walls[i - 2][j - 1].append((1, 0))
    elif d == 1:
        walls[i - 1][j - 1].append((0, 1))
        walls[i - 1][j].append((0, -1))

t = 0
while True:
    if t > 100:
        break

    # 바람 방출
    for i, j, d in airs:
        di, dj = d_list[d]
        ni, nj = i + di, j + dj
        v = [[0] * M for _ in range(N)]
        heat(ni, nj, d, 0)

    # 온도 조절
    new_arr = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            for di, dj in d_list:
                ni, nj = i + di, j + dj
                if 0 <= ni < N and 0 <= nj < M and arr[i][j] - arr[ni][nj] >= 4 and not (di, dj) in walls[i][j]:
                    new_arr[ni][nj] += (arr[i][j] - arr[ni][nj]) // 4
                    new_arr[i][j] -= (arr[i][j] - arr[ni][nj]) // 4
    for i in range(N):
        for j in range(M):
            arr[i][j] += new_arr[i][j]

    # 바깥 온도 감소
    for i in range(N):
        for j in range(M):
            if (i == 0 or i == N - 1 or j == 0 or j == M - 1) and arr[i][j]:
                arr[i][j] -= 1

    # 초콜릿 섭취
    t += 1

    # 온도 조사
    for si, sj in sensors:
        if arr[si][sj] < K:
            break
    else:
        break

print(t)