# 12100. 2048(Easy) 2022-04-10

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

blocks = []
for i in range(N):
    for j in range(N):
        if arr[i][j] != 0:
            blocks.append((i, j, arr[i][j]))

cnt = 0
d = -1
# 위로
blocks.sort()
moved = []
for i, j, num in blocks:
    while 0 <= i < N and not (i, j, num) in moved:
        i -= 1
