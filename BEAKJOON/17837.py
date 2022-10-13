# 17837. 새로운 게임2  2022-10-12


def move(i, j, ni, nj, k):
    idx = p_arr[i][j].index(k)
    move_p = p_arr[i][j][idx:]
    p_arr[i][j] = p_arr[i][j][:idx]
    for p in move_p:
        pieces[p] = [ni, nj, pieces[p][2]]

    if arr[ni][nj] == 1:
        move_p.reverse()
    p_arr[ni][nj].extend(move_p)


d_list = [(0, 1), (0, -1), (-1, 0), (1, 0)]
N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
p_arr = [[[] for _ in range(N)] for _ in range(N)]
pieces = dict()
for k in range(1, K + 1):
    i, j, d = list(map(int, input().split()))
    p_arr[i - 1][j - 1].append(k)
    pieces[k] = [i - 1, j - 1, d - 1]

t = 0
chk = False
while t <= 1000:
    t += 1

    for k in range(1, K + 1):
        i, j, d = pieces[k]
        di, dj = d_list[d]
        ni, nj = i + di, j + dj

        if not 0 <= ni < N or not 0 <= nj < N or arr[ni][nj] == 2:
            ni, nj = i - di, j - dj
            pieces[k][2] = 2 * (pieces[k][2] // 2) + 1 - (pieces[k][2] % 2)
            if not 0 <= ni < N or not 0 <= nj < N or arr[ni][nj] == 2:
                ni, nj = i, j
                pass
            else:
                move(i, j, ni, nj, k)
        else:
            move(i, j, ni, nj, k)

        if len(p_arr[ni][nj]) >= 4:
            chk = True
            break
    if chk:
        break

if t > 1000:
    print(-1)
else:
    print(t)