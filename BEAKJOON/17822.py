# 17822. 원판 돌리기 G3 2022-04-29


N, M, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

for _ in range(T):
    x, d, k = map(int, input().split())  # x판을 d방향으로, k칸 회전
    k %= M
    x -= 1

    for i in range(x, N):
        if (i + 1) % (x + 1) == 0:
            if d == 0:  # 시계 방향이면
                arr[i] = arr[i][M - k:] + arr[i][:M - k]
            else:
                arr[i] = arr[i][k:] + arr[i][:k]

    chk = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] != 0:
                num = arr[i][j]
                q = [(i, j)]
                while q:
                    ii, jj = q.pop(0)
                    for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                        ni, nj = ii + di, jj + dj
                        if nj == M:
                            nj = 0
                        elif nj == -1:
                            nj = M - 1
                        if 0 <= ni < N and arr[ni][nj] == num:
                            chk = 1
                            q.append((ni, nj))
                            arr[ni][nj] = 0

    if chk == 0:
        tot = 0
        cnt = 0
        for i in range(N):
            for j in range(M):
                if arr[i][j]:
                    tot += arr[i][j]
                    cnt += 1
        if cnt == 0:
            print(0)
            exit(0)
        else:
            avg = tot / cnt

        for i in range(N):
            for j in range(M):
                if arr[i][j]:
                    if arr[i][j] > avg:
                        arr[i][j] -= 1
                    elif arr[i][j] < avg:
                        arr[i][j] += 1

ans = 0
for i in range(N):
    for j in range(M):
        if arr[i][j]:
            ans += arr[i][j]

print(ans)