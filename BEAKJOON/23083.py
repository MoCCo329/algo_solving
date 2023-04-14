# 23083. 꿀벌 승연이  2023-04-14


N, M = map(int, input().split())
maps = [[0] * M for _ in range(N)]
for _ in range(int(input())):
    i, j = map(lambda x: int(x) - 1, input().split())
    maps[i][j] = -1

div_n = int(1e9 + 7)
for i in range(N):
    if maps[i][0] == -1: break
    maps[i][0] = 1

for j in range(1, M):
    for i in range(N):
        if maps[i][j] == -1: continue

        a = maps[i - 1][j]
        b = maps[i][j - 1]
        c = -1
        if j % 2 == 0 and i != 0:
            c = maps[i - 1][j - 1]
        elif j % 2 == 1 and i != N - 1:
            c = maps[i + 1][j - 1]

        if a != -1:
            maps[i][j] += a
        if b != -1:
            maps[i][j] += b
        if c != -1:
            maps[i][j] += c

        maps[i][j] = maps[i][j] % div_n

print(maps[N - 1][M - 1])