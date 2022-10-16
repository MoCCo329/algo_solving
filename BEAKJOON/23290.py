# 23290. 마법사 상어와 복제  2022-10-16


def move_shark(path, n, kill):
    global temp_kill, temp_path

    if n == 3:
        if kill > temp_kill:
            temp_kill = kill
            temp_path = path[1:]
        elif not temp_path:
            temp_path = path[1:]
        return

    i, j = path[-1]
    for di, dj in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        ni, nj = i + di, j + dj
        if 0 <= ni < 4 and 0 <= nj < 4:
            move_shark(path + [(ni, nj)], n + 1, kill if (ni, nj) in path[1:] else kill + arr[ni][nj])


d_list = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
M, S = map(int, input().split())
fishes = dict()
f_num = M
for k in range(1, M + 1):
    fishes[k] = list(map(lambda x:int(x) - 1, input().split()))
si, sj = map(lambda x:int(x) - 1, input().split())


v = [[0] * 4 for _ in range(4)]  # 물고기 냄새
for t in range(1, S + 1):
    # 물고기 이동
    arr = [[0] * 4 for _ in range(4)]  # 물고기 표시
    new_fishes = dict()
    nf_num = 0
    for k in range(1, f_num + 1):
        if not fishes[k]: continue
        fi, fj, d = fishes[k]
        nf_num += 1
        for _ in range(8):
            di, dj = d_list[d]
            ni, nj = fi + di, fj + dj
            if not 0 <= ni < 4 or not 0 <= nj < 4 or (si, sj) == (ni, nj) or v[ni][nj]:
                d = (d - 1) % 8
                continue
            break
        else:
            ni, nj = fi, fj
        new_fishes[nf_num] = [ni, nj, d]
        arr[ni][nj] += 1

    # 상어 이동
    temp_kill = 0
    temp_path = []
    move_shark([(si, sj)], 0, 0)
    for k in range(1, nf_num + 1):
        fi, fj, d = new_fishes[k]
        if (fi, fj) in temp_path:
            new_fishes[k] = 0
            v[fi][fj] = 3
    si, sj = temp_path[-1]

    # 냄새 제거
    for i in range(4):
        for j in range(4):
            if v[i][j]:
                v[i][j] -= 1

    # 복제
    for k in range(1, nf_num + 1):
        fishes[f_num + k] = new_fishes[k]
    f_num += nf_num

ans = 0
for k in range(1, f_num + 1):
    if fishes[k]:
        ans += 1
print(ans)