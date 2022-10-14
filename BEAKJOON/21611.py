# 21611. 마법사 상어와 블리자드  2022-10-14


def next_pos(i, j):
    if (i, j) == (L, L):
        d = 0
    elif i > L:
        if i <= j:
            d = 3
        elif j < N - 1 - i:
            d = 1
        else:
            d = 2
    else:
        if j > N - 1 - i:
            d = 3
        elif j < i:
            d = 1
        else:
            d = 0

    di, dj = d_list[d]
    ni, nj = i + di, j + dj

    return (ni, nj)


def move():
    i, j = next_pos(L, L)
    t = 1
    while t < N ** 2 - 1:
        ni, nj = next_pos(i, j)
        t += 1
        temp_t = t
        while temp_t < N ** 2 - 1 and not arr[ni][nj]:
            ni, nj = next_pos(ni, nj)
            temp_t += 1

        if not arr[ni][nj]: return
        if not arr[i][j]:
            arr[i][j] = arr[ni][nj]
            arr[ni][nj] = 0
        i, j = next_pos(i, j)


def boom():
    global chk

    i, j = next_pos(L, L)
    t = 1
    while t < N ** 2 - 1:
        cnt = 1
        ni, nj = next_pos(i, j)
        t += 1
        while t < N ** 2 - 1 and arr[i][j] and arr[i][j] == arr[ni][nj]:
            cnt += 1
            ni, nj = next_pos(ni, nj)
            t += 1

        if cnt >= 4:
            chk = True
            ans[arr[i][j]] += cnt
            while cnt > 0:
                arr[i][j] = 0
                cnt -= 1
                i, j = next_pos(i, j)

        i, j = ni, nj


def change():
    new_arr = []

    i, j = next_pos(L, L)
    t = 1
    while t < N ** 2 - 1:
        if not arr[i][j]: break

        cnt = 1
        ni, nj = next_pos(i, j)
        t += 1
        while t < N ** 2 - 1 and arr[i][j] == arr[ni][nj]:
            cnt += 1
            ni, nj = next_pos(ni, nj)
            t += 1

        new_arr.append(cnt)
        new_arr.append(arr[i][j])
        i, j = ni, nj

    i, j = next_pos(L, L)
    t = 1
    while t < N ** 2:
        if t <= len(new_arr):
            arr[i][j] = new_arr[t - 1]
        else:
            arr[i][j] = 0
        i, j = next_pos(i, j)
        t += 1



d_list = [(0, -1), (1, 0), (0, 1), (-1, 0)]
N, M = map(int, input().split())
L = N // 2
arr = [list(map(int, input().split())) for _ in range(N)]
magics = [list(map(int, input().split())) for _ in range(M)]
ans = [0, 0, 0, 0]

for k in range(M):
    d, s = magics[k]
    
    # 구슬 파괴
    di, dj = [(-1, 0), (1, 0), (0, -1), (0, 1)][d - 1]
    for ss in range(1, s + 1):
        ni, nj = L + ss * di, L + ss * dj
        if 0 <= ni < N and 0 <= nj < N:
            arr[ni][nj] = 0
    
    # 구슬 이동
    move()

    # 구슬 폭발
    chk = True  # 폭발 여부
    while chk:
        chk = False
        boom()
        move()
    
    # 구슬 변화
    change()

tot = 0
for i in range(1, 4):
    tot += ans[i] * i
print(tot)