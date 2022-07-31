# 16724. 피리 부는 사나이  2022-07-31


N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
v = [[0] * M for _ in range(N)]

cnt = 0
for i in range(N):
    for j in range(M):
        if v[i][j] == 0:
            path = []
            cnt += 1
            ii, jj = i, j
            while True:
                path.append((ii, jj))
                v[ii][jj] = cnt
                di, dj = {'D': (1, 0), 'U': (-1, 0), 'L': (0, -1), 'R': (0, 1)}[arr[ii][jj]]
                ni, nj = ii + di, jj + dj
                if v[ni][nj] and v[ni][nj] != cnt:
                    cnt -= 1
                    temp = v[ni][nj]
                    for iii, jjj in path:
                        v[iii][jjj] = temp
                    break
                elif v[ni][nj] == cnt:
                    break
                else:
                    ii, jj = ni, nj

print(cnt)