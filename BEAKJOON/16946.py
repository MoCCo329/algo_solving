# 16946. 벽 부수고 이동하기 4  2023-01-14


from collections import deque


def dfs(i, j):
    global tag_i

    q = deque()
    q.append((i, j))
    v[i][j] = tag_i
    cnt = 1

    while q:
        ii, jj = q.pop()
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ni, nj = ii + di, jj + dj
            if 0 <= ni < N and 0 <= nj < M and v[ni][nj] == -1 and maps[ni][nj] == 0:
                v[ni][nj] = tag_i
                cnt += 1
                q.append((ni, nj))

    tag.append(cnt)
    tag_i += 1


N, M = map(int, input().split())
maps = [list(map(int, input())) for _ in range(N)]
v = [[-1] * M for _ in range(N)]

tag = []
tag_i = 0  # v에 tag_i으로 저장. tag 의 tag_i 인덱스에는 갈 수 있는 칸들의 개수가 담긴다.
for i in range(N):
    for j in range(M):
        if maps[i][j] == 0: continue

        tag_i_set = set()
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ni, nj = i + di, j + dj
            if not (0 <= ni < N) or not (0 <= nj < M) or maps[ni][nj] != 0: continue

            if v[ni][nj] == -1: dfs(ni, nj)
            tag_i_set.add(v[ni][nj])

        cnt = 1
        for tag_idx in tag_i_set:
            cnt += tag[tag_idx]
        maps[i][j] = cnt

for i in range(N):
    print(*[maps[i][j] % 10 for j in range(M)], sep="")