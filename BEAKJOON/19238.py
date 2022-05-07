# 19238 스타트 택시 G2 2022-05-07


def findCustomer(si, sj):
    if arr[si][sj] == 2:
        return si, sj, 0

    res = []
    minD = 100
    v = [[0] * N for _ in range(N)]
    v[si][sj] = 1
    q = []
    q.append([si, sj])
    while q:
        i, j = q.pop(0)
        if minD < v[i][j]:
            break
        for di, dj in [[-1, 0], [0, -1], [0, 1], [1, 0]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N and v[ni][nj] == 0 and arr[ni][nj] != 1:
                if arr[ni][nj] == 2:
                    res.append([ni, nj])
                    minD = v[i][j]
                    q.append([ni, nj])
                    v[ni][nj] = v[i][j] + 1
                else:
                    q.append([ni, nj])
                    v[ni][nj] = v[i][j] + 1
    if res:
        res.sort(key = lambda x: (x[0], x[1]))
        return res[0] + [minD]
    return -1, -1, -1


def findDestination(ci, cj, fi, fj):
    v = [[0] * N for _ in range(N)]
    v[ci][cj] = 1
    q = []
    q.append([ci, cj])
    while q:
        i, j = q.pop(0)
        for di, dj in [[-1, 0], [0, -1], [0, 1], [1, 0]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N and v[ni][nj] == 0 and arr[ni][nj] != 1:
                if ni == fi and nj == fj:
                    return v[i][j]
                else:
                    q.append([ni, nj])
                    v[ni][nj] = v[i][j] + 1
    return -1


N, M, B = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
i, j = map(int, input().split())
start = [i - 1, j - 1]
cList = []
for _ in range(M):
    ci, cj, fi, fj = map(int, input().split())
    arr[ci - 1][cj - 1] = 2
    cList.append([ci - 1, cj - 1, fi - 1, fj - 1])

while M:
    si, sj = start
    ci, cj, d1 = findCustomer(si, sj)
    arr[ci][cj] = 0
    if B > d1 and d1 != -1:
        B -= d1
    else:
        B = -1
        break

    for i in range(M):
        if cList[i][:2] == [ci, cj]:
            fi, fj = cList[i][2:]
            cList.pop(i)
            M -= 1
            break

    d2 = findDestination(ci, cj, fi, fj)
    if B >= d2 and d2 != -1:
        B -= d2
    else:
        B = -1
        break

    start = [fi, fj]
    B += d2 * 2

print(B)