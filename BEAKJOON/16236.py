# 16236. 아기 상어 2022-04-23


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
shark = []
shark_size = [2, 0]

for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            shark = [i, j]
            arr[i][j] = 0

ans = 0
while True:
    v = [[0] * N for _ in range(N)]
    i, j = shark[0], shark[1]
    q = [(i, j)]
    v[i][j] = 1
    min_dist = 300
    next = []
    while q:
        i, j = q.pop(0)
        for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N and v[ni][nj] == 0 and arr[ni][nj] <= shark_size[0]:
                dist = v[i][j] + 1
                if 0 < arr[ni][nj] < shark_size[0] and dist <= min_dist:
                    min_dist = dist
                    if next:
                        if ni < next[0]:
                            next = [ni, nj]
                        elif ni == next[0] and nj < next[1]:
                            next = [ni, nj]
                    else:
                        next = [ni, nj]
                elif not next:
                    q.append((ni, nj))
                    v[ni][nj] = dist

    if not next:
        break

    shark = next[::]
    arr[next[0]][next[1]] = 0
    if shark_size[1] + 1 == shark_size[0]:
        shark_size[0] += 1
        shark_size[1] = 0
    else:
        shark_size[1] += 1

    ans += min_dist - 1

print(ans)