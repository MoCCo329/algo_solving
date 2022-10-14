# 삼성 SW 역량테스트 2022 상반기 오전 2번문제. 술래잡기


def move_runner():
    for k in range(1, M + 1):
        if not runers[k]: continue
        ri, rj, rd = runers[k]
        if abs(i - ri) + abs(j - rj) > 3: continue

        di, dj = d_list[rd]
        ni, nj = ri + di, rj + dj
        if 0 <= ni < N and 0 <= nj < N:
            if (ni, nj) != (i, j):
                ri, rj = ni, nj
        else:
            rd = (rd + 2) % 4
            ni, nj = ri - di, rj - dj
            if (ni, nj) != (i, j):
                ri, rj = ni, nj
        runers[k] = [ri, rj, rd]


def move_tagger():
    global i, j, d, d_state

    di, dj = d_list[d]
    i, j = i + di, j + dj

    chk = False
    if (i, j) == (0, 0):
        d = 2
        d_state = True
    elif (i, j) == (N // 2, N // 2):
        d = 0
        d_state = False
    elif (i > N // 2 and i == j) or i == abs(N - 1 - j):
        chk = True
    elif i < N // 2 and i + 1 == j:
        chk = True

    if chk:
        if d_state:
            d = (d - 1) % 4
        else:
            d = (d + 1) % 4


def catch():
    global ans

    di, dj = d_list[d]
    cnt = 0  # 잡은 도망자 수
    for s in range(3):
        ni, nj = i + s * di, j + s * dj
        if not 0 <= ni < N or not 0 <= nj < N: break
        if arr[ni][nj]: continue
        for k in range(1, M + 1):
            if not runers[k]: continue
            ri, rj, rd = runers[k]
            if (ni, nj) == (ri, rj):
                cnt += 1
                runers[k] = 0
    ans += cnt * t


d_list = [(-1, 0), (0, 1), (1, 0), (0, -1)]
N, M, H, K = map(int, input().split())
arr = [[0] * N for _ in range(N)]
runers = dict()
for k in range(1, M + 1):
    ri, rj, rd = map(int, input().split())
    runers[k] = [ri - 1, rj - 1, rd]
for _ in range(H):
    ti, tj = map(lambda x: int(x) - 1, input().split())
    arr[ti][tj] = 1

i, j = N // 2, N // 2  # 술래 위치
d = 0  # 술래 방향
d_state = False  # False이면 멀어지기, True이면 되돌아오기
ans = 0
for t in range(1, K + 1):
    # 도망자 이동
    move_runner()
    
    # 술래 이동
    move_tagger()
    
    # 술래 잡기
    catch()

print(ans)