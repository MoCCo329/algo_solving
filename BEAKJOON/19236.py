# 19236. 청소년 상어  2022-10-10


arr = [[0] * 4 for _ in range(4)]  # 상어는 0이다. 빈칸은 -1 이다.
fishes = dict()  # 상어는 0번에 담긴다. 먹힌 물고기 정보는 0 이다.
for i in range(4):
    line = list(map(int, input().split()))
    for j in range(4):
        a, b = line[j * 2], line[j * 2 + 1]
        arr[i][j] = a
        fishes[a] = (i, j, b)

# 상어 시작
start = arr[0][0]
fishes[0] = (0, 0, fishes[start][2])
fishes[start] = 0
arr[0][0] = 0

ans = 0
def dfs(tot):
    global ans, fishes, arr

    # 물고기 이동
    for i in range(1, 17):
        fish = fishes.get(i, 0)
        if fish:
            i, j, d_idx = fish
            while True:
                d = [(-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1)][d_idx % 8]
                di, dj = d
                ni, nj = i + di, j + dj
                if 0 <= ni < 4 and 0 <= nj < 4 and arr[ni][nj] != 0:
                    break
                d_idx += 1
            move_f = arr[i][j]  # 움직이는 물고기
            change_f = arr[ni][nj]  # 자리 바뀌는 물고기
            arr[i][j], arr[ni][nj] = change_f, move_f
            fishes[move_f] = (ni, nj, d_idx)
            if change_f != -1:
                fishes[change_f] = (i, j, fishes[change_f][2])

    # 상어 이동
    i, j, d_idx = fishes[0]
    di, dj = [(-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1)][d_idx % 8]
    chk = False  # 물고기 먹을 수 있는지
    for k in range(1, 4):
        ni, nj = i + di * k, j + dj * k
        if 0 <= ni < 4 and 0 <= nj < 4 and arr[ni][nj] != -1:
            chk = True

            temp_fishes = { i: fishes[i] for i in range(17) }
            temp_arr = [[arr[i][j] for j in range(4)] for i in range(4)]

            change_f = arr[ni][nj]  # 먹히는 물고기
            change_f_info = fishes[change_f]
            fishes[0] = (ni, nj, change_f_info[2])
            fishes[change_f] = 0
            arr[ni][nj] = 0
            arr[i][j] = -1
            # dfs
            dfs(tot + change_f)
            # 다시 되돌리기
            arr = temp_arr[::]
            fishes = { i: temp_fishes[i] for i in range(17) }
    if not chk:
        ans = max(ans, tot)


dfs(start)
print(ans)