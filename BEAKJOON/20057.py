# 20057. 마법사 상어와 토네이도  2022-10-12


def move(i, j, d_idx):
    global arr

    tot = arr[i][j]
    leftover = tot
    arr[i][j] = 0
    out = 0

    # 10%
    for di, dj in [(-1, -1), (1, -1)]:
        if d_idx == 1:
            di, dj = -dj, di
        elif d_idx == 2:
            dj = -dj
        elif d_idx == 3:
            di, dj = dj, di

        ni, nj = i + di, j + dj
        temp = int(tot / 100 * 10)
        if 0 <= ni < N and 0 <= nj < N:
            arr[ni][nj] += temp
        else:
            out += temp
        leftover -= temp

    # 7%
    for di, dj in [(-1, 0), (1, 0)]:
        if d_idx == 1:
            di, dj = -dj, di
        elif d_idx == 2:
            dj = -dj
        elif d_idx == 3:
            di, dj = dj, di

        ni, nj = i + di, j + dj
        temp = int(tot / 100 * 7)
        if 0 <= ni < N and 0 <= nj < N:
            arr[ni][nj] += temp
        else:
            out += temp
        leftover -= temp

    # 5%
    for di, dj in [(0, -2)]:
        if d_idx == 1:
            di, dj = -dj, di
        elif d_idx == 2:
            dj = -dj
        elif d_idx == 3:
            di, dj = dj, di

        ni, nj = i + di, j + dj
        temp = int(tot / 100 * 5)
        if 0 <= ni < N and 0 <= nj < N:
            arr[ni][nj] += temp
        else:
            out += temp
        leftover -= temp

    # 2%
    for di, dj in [(-2, 0), (2, 0)]:
        if d_idx == 1:
            di, dj = -dj, di
        elif d_idx == 2:
            dj = -dj
        elif d_idx == 3:
            di, dj = dj, di

        ni, nj = i + di, j + dj
        temp = int(tot / 100 * 2)
        if 0 <= ni < N and 0 <= nj < N:
            arr[ni][nj] += temp
        else:
            out += temp
        leftover -= temp

    # 1%
    for di, dj in [(-1, 1), (1, 1)]:
        if d_idx == 1:
            di, dj = -dj, di
        elif d_idx == 2:
            dj = -dj
        elif d_idx == 3:
            di, dj = dj, di

        ni, nj = i + di, j + dj
        temp = int(tot / 100 * 1)
        if 0 <= ni < N and 0 <= nj < N:
            arr[ni][nj] += temp
        else:
            out += temp
        leftover -= temp

    # a
    for di, dj in [(0, -1)]:
        if d_idx == 1:
            di, dj = -dj, di
        elif d_idx == 2:
            dj = -dj
        elif d_idx == 3:
            di, dj = dj, di

        ni, nj = i + di, j + dj
        if 0 <= ni < N and 0 <= nj < N:
            arr[ni][nj] += leftover
        else:
            out += leftover

    return out


d_list = [(0, -1), (1, 0), (0, 1), (-1, 0)]
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
i, j = N // 2, N // 2
t = 0

ans = 0
while t < (N - 1) * 2 + 1:
    di, dj = d_list[t % 4]
    length = t // 2 + 1
    for _ in range(length):
        i, j = i + di, j + dj
        if not 0 <= i < N or not 0 <= j < N:
            break
        ans += move(i, j, t % 4)
    t += 1

print(ans)