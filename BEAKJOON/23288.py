# 23288. 주사위 굴리기2  2022-10-10


def move_i(i):
    i %= 4
    if not i: return

    temp = [dice[0][1], dice[1][1], dice[2][1], dice[3][1]]
    temp = temp[i:] + temp[:i]
    dice[0][1] = temp[0]
    dice[1][1] = temp[1]
    dice[2][1] = temp[2]
    dice[3][1] = temp[3]


def move_j(j):
    j %= 4
    if not j: return

    temp = [*dice[1], dice[3][1]]
    temp = temp[j:] + temp[:j]
    dice[1] = temp[:3]
    dice[3][1] = temp[3]


def score(si, sj):
    v = [[0] * M for _ in range(N)]
    v[si][sj] = 1
    q = [(si, sj)]
    s = 1

    while q:
        i, j = q.pop(0)
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M and not v[ni][nj] and arr[ni][nj] == arr[si][sj]:
                s += 1
                v[ni][nj] = 1
                q.append((ni, nj))

    return s


dice = [[0, 2, 0], [4, 6, 3], [0, 5, 0], [0, 1, 0]]
N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
i, j = 0, 0
d = [[0, 1], [1, 0], [0, -1], [-1, 0]]
d_idx = 0
ans = 0

for turn in range(K):
    # 주사위 이동
    di, dj = d[d_idx]
    ni, nj = i + di, j + dj
    if not (0 <= ni < N) or not (0 <= nj < M):
        d_idx = (d_idx + 2) % 4
        di, dj = d[d_idx]
        ni, nj = i + di, j + dj
    move_i(di)
    move_j(dj)
    i, j = ni, nj
    
    # 방향 전환
    if dice[1][1] > arr[i][j]:
        d_idx = (d_idx + 1) % 4
    elif dice[1][1] < arr[i][j]:
        d_idx = (d_idx - 1) % 4
    
    # 점수 계산
    ans += score(i, j) * arr[i][j]

print(ans)