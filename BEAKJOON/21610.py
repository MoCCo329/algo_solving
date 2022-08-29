# 21610. 마법사 상어와 비바라기  2022-08-29


move_dict = { 1: (0, -1), 2: (-1, -1), 3: (-1, 0), 4: (-1, 1), 5: (0, 1), 6: (1, 1), 7: (1, 0), 8: (1, -1) }

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
moves = []
for _ in range(M):
    d, s = map(int, input().split())
    di, dj = move_dict[d]
    moves.append((di * s, dj * s))

clouds = [(N - 1, 0), (N - 1, 1), (N - 2, 0), (N - 2, 1)]

while moves:
    di, dj = moves.pop(0)
    new_clouds = []
    for i in range(len(clouds)):
        ni, nj = (clouds[i][0] + di) % N, (clouds[i][1] + dj) % N
        arr[ni][nj] += 1
        new_clouds.append((ni, nj))

    for i, j in new_clouds:
        for di, dj in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj]:
                arr[i][j] += 1

    clouds = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] >= 2 and (i, j) not in new_clouds:
                arr[i][j] -= 2
                clouds.append((i, j))

ans = 0
for i in range(N):
    ans += sum(arr[i])
print(ans)