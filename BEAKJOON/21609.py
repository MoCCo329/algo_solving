# 21609 G2 상어 중학교 2022-05-15


def bfs(si, sj):
    color = arr[si][sj]
    q = []
    q.append([si, sj])
    blocks = []
    blocks.append([si, sj])
    rainbowBlocks = []
    rainbowNum = 0
    v[si][sj] = 1
    while q:
        i, j = q.pop(0)
        for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N and v[ni][nj] == 0 and (arr[ni][nj] == 0 or arr[ni][nj] == color):
                q.append([ni, nj])
                if arr[ni][nj] == 0:
                    rainbowBlocks.append([ni, nj])
                    rainbowNum += 1
                else:
                    blocks.append([ni, nj])
                v[ni][nj] = 1

    for i, j in rainbowBlocks:
        v[i][j] = 0
    if len(blocks) + len(rainbowBlocks) == 1:
        v[si][sj] = 0
        return 0
    else:
        blocks.sort()
        return blocks + rainbowBlocks + [rainbowNum]


def gravity():
    for j in range(N):
        for i in range(N - 1, -1, -1):
            if arr[i][j] >= 0:
                ni = i + 1
                nni = i
                while ni < N and arr[ni][j] == -2:
                    arr[ni][j] = arr[nni][j]
                    arr[nni][j] = -2
                    ni += 1
                    nni += 1


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0

while True:
    blockList = []  # 배열 마지막엔 무지개블록의 개수가 담긴다.
    v = [[0] * N for _ in range(N)]
    # 블록 그룹들 찾기
    for i in range(N):
        for j in range(N):
            if arr[i][j] > 0 and v[i][j] == 0:  # 일반블록이면
                blockTemp = bfs(i, j)
                if blockTemp:
                    blockList.append(blockTemp)

    if len(blockList) == 0:
        break
    blockList.sort(key=lambda x: (len(x), x[-1], x[0][0], x[0][1]), reverse=True)


    # 가장 큰 그룹 찾아 없애기
    block = blockList[0]
    ans += (len(block) - 1) ** 2

    for k in range(len(block) - 1):
        i, j = block[k]
        arr[i][j] = -2
    # 중력작용
    gravity()
    # 돌리기
    arr = [[arr[i][j] for i in range(N)] for j in range(N - 1, -1, -1)]
    # 중력작용
    gravity()

print(ans)