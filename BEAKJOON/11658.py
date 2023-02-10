# 11658. 구간 합 구하기3  2023-02-10


import sys
input = sys.stdin.readline


N, M = map(int, input().split())
k = 1
while k < N: k <<= 1
st = [[0] * N for _ in range(k)] + [list(map(int, input().split())) for _ in range(N)] + [[0] * N for _ in range(k - N)]
for i in range(k - 1, 0, -1):
    for j in range(N):
        st[i][j] = st[i * 2][j] + st[i * 2 + 1][j]

for _ in range(M):
    line = list(map(int, input().split()))
    if line[0] == 0:
        i, j = line[1:3]
        st[i + k - 1][j - 1] = line[3]

        i = (i + k - 1) // 2
        while i > 0:
            st[i][j - 1] = st[i * 2][j - 1] + st[i * 2 + 1][j - 1]
            i >>= 1
    else:
        x1, y1, x2, y2 = line[1:]

        tot = 0
        x1 += k - 1
        x2 += k - 1
        while x1 <= x2:
            if x1 & 1: tot += sum(st[x1][y1 - 1:y2])
            if not x2 & 1: tot += sum(st[x2][y1 - 1:y2])
            x1 = (x1 + 1) // 2
            x2 = (x2 - 1) // 2
        print(tot)