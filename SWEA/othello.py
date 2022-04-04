d = [1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]

def fillin(i, j, color):
    arr[i][j] = color
    for di, dj in d:
        ni, nj = i + di, j + dj
        s = []

        while 0 <= ni < N and 0 <= nj < N and arr[ni][nj] != 0:
            if arr[ni][nj] == color:
                while s:
                    nni, nnj = s.pop()
                    arr[nni][nnj] = color
                break
            else:
                s.append((ni, nj))
                ni, nj = ni + di, nj + dj

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[0]*N for _ in range(N)]
    arr[N//2-1][N//2] = 1  # 흰 돌
    arr[N//2][N//2-1] = 1
    arr[N//2-1][N//2-1] = 2  # 검은 돌
    arr[N//2][N//2] = 2

    for _ in range(M):
        i, j, color = map(int, input().split())
        fillin(i-1, j-1, color)

    B = 0
    W = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                B += 1
            if arr[i][j] == 2:
                W += 1

    print(f'#{tc} {B} {W}')