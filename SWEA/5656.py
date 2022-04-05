# 5656. 벽돌 깨기 2022-04-05

def breaking(kk, N):  # kk는 구슬 횟수
    global ans
    if ans == 0:
        return
    # 도착한 경우
    elif kk == N:
        cnt = 0
        for i in range(W):
            for j in range(H):
                if n_arr[i][j] != 0:
                    cnt += 1
        if ans > cnt:
            ans = cnt
        return

    # 꺠지는 벽돌들 찾기
    chk = 0  # 벽돌이 없는 경우 체크
    for i in range(W):
        v = [[0] * H for _ in range(W)]
        j = H - 1
        while n_arr[i][j] == 0 and j > 0:  # 처음 부딪히는 벽돌 찾기
            j -= 1
        if n_arr[i][j] == 0:  # 열이 빈 경우
            chk += 1
            continue
        q = [(i, j)]
        v[i][j] = n_arr[i][j]
        while q:
            ii, jj = q.pop(0)
            for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                for k in range(1, n_arr[ii][jj]):
                    ni, nj = ii + di * k, jj + dj * k
                    if 0 <= ni < W and 0 <= nj < H and v[ni][nj] == 0 and n_arr[ni][nj] != 0:
                        q.append((ni, nj))
                        v[ni][nj] = n_arr[ni][nj]

        # 벽돌 깨기
        for i in range(W):
            for j in range(H - 1, -1, -1):
                if v[i][j] != 0:
                    n_arr[i].pop(j)
            n_arr[i] = n_arr[i] + [0] * (H - len(n_arr[i]))

        # 다음 구슬로
        breaking(kk + 1, N)

        # 깨진 벽돌 복원
        for i in range(W):
            for j in range(H):
                if v[i][j] != 0:
                    n_arr[i].insert(j, v[i][j])
            if len(n_arr[i]) >= H:
                n_arr[i] = n_arr[i][:H]

    # 벽돌이 0개인 경우
    else:
        if chk == W:
            ans = 0
            return


T = int(input())
for tc in range(1, T + 1):
    N, W, H = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(H)]
    n_arr = []
    for j in range(W):
        n_arr.append([arr[i][j] for i in range(H - 1, -1, -1)])
    ans = 180

    breaking(0, N)
    print(f'#{tc} {ans}')