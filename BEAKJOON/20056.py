# 20056. 마법사 상어와 파이어볼  2022-0-10-11


N, M, K = map(int, input().split())
arr = [[0] * N for _ in range(N)]
d_list = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
fires = dict()
end = M

for k in range(1, M + 1):
    i, j, m, s, d = map(int, input().split())
    arr[i - 1][j - 1] = k
    fires[k] = [i - 1, j - 1, m, s, d]

for _ in range(K):
    new_arr = [[0] * N for _ in range(N)]
    # 이동
    for k in range(1, end + 1):
        if not fires[k]: continue
        i, j, m, s, d = fires[k]
        di, dj = d_list[d]
        ni, nj = (i + di * s) % N, (j + dj * s) % N
        if new_arr[ni][nj] == 0:
            new_arr[ni][nj] = k
        elif type(new_arr[ni][nj]) == int:
            new_arr[ni][nj] = [new_arr[ni][nj], k]
        else:
            new_arr[ni][nj] = [*new_arr[ni][nj], k]
        fires[k] = [ni, nj, m, s, d]
    
    # 합체
    arr = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if type(new_arr[i][j]) == int:
                arr[i][j] = new_arr[i][j]
                continue

            new_m, new_s, cnt = 0, 0, 0
            chk1 = True  # 모두 짝수인지
            chk2 = True  # 모두 홀수인지
            for k in new_arr[i][j]:
                cnt += 1
                new_m += fires[k][2]
                new_s += fires[k][3]
                if fires[k][4] % 2:
                    chk1 = False
                else:
                    chk2 = False
                fires[k] = 0
            new_m //= 5
            new_s //= cnt
            new_d = (0, 2, 4, 6) if (chk1 or chk2) else (1, 3, 5, 7)
            if not new_m:
                continue
            arr[i][j] = [end + i for i in range(1, 5)]
            for c in range(1, 5):
                fires[end + c] = [i, j, new_m, new_s, new_d[c - 1]]
            end += 4

ans = 0
for k in range(1, end + 1):
    if not fires[k]: continue
    ans += fires[k][2]
print(ans)