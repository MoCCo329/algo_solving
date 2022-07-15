# 2638. 치즈  2022-07-15


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 외부 확인
q = [(0, 0)]
arr[0][0] = -1
while q:
    i, j = q.pop(0)
    for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
        ni, nj = i + di, j + dj
        if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 0:
            q.append((ni, nj))
            arr[ni][nj] = -1

ans = 0
while True:
    # 지우기
    pop_set = set()
    for i in range(1, N - 1):
        for j in range(1, M - 1):
            if arr[i][j] == 1:
                cnt = 0
                for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == -1:
                        cnt += 1
                if cnt >= 2:
                    pop_set.add((i, j))

    if pop_set:
        ans += 1
        for i, j in pop_set:
            arr[i][j] = -1
    else:
        break

    # 외부 확인
    for i in range(1, N - 1):
        for j in range(1, M - 1):
            if arr[i][j] == 0:
                for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == -1:
                        q = [(i, j)]
                        arr[i][j] = -1
                        while q:
                            ii, jj = q.pop(0)
                            for ddi, ddj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                                nni, nnj = ii + ddi, jj + ddj
                                if 0 <= nni < N and 0 <= nnj < M and arr[nni][nnj] == 0:
                                    q.append((nni, nnj))
                                    arr[nni][nnj] = -1

print(ans)