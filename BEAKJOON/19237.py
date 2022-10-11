# 19237. 어른 상어  2022-10-11


N, M, K = map(int, input().split())
arr = []
sharks = dict()
for i in range(N):
    line = list(map(lambda x: [int(x)], input().split()))
    for j in range(N):
        if line[j][0] != 0:
            sharks[line[j][0]] = (i, j)
    arr.append(line)

d = [0] + list(map(int, input().split()))
d_list = [0, (-1, 0), (1, 0), (0, -1), (0, 1)]

moves = dict()
for i in range(1, M + 1):
    move = dict()
    for j in range(1, 5):
        move[j] = list(map(int, input().split()))
    moves[i] = move

t = 0
v = [[[0, 0] for _ in range(N)] for _ in range(N)]  # 0에 상어 번호, 1에 남은 지속 시간
while t <= 1000:
    # 냄새 뿌리기
    cnt = 0
    for k in range(1, M + 1):
        if not sharks[k]: continue
        cnt += 1
        i, j = sharks[k]
        v[i][j] = [k, K]
    if cnt == 1:
        break

    # 이동
    new_arr = [[[0] for _ in range(N)] for _ in range(N)]
    for k in range(1, M + 1):
        if not sharks[k]: continue

        i, j = sharks[k]
        temp1 = []
        temp2 = []
        for d_idx in moves[k][d[k]]:
            di, dj = d_list[d_idx]
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N:
                if v[ni][nj][0] == 0:
                    temp1.append((ni, nj))
                elif v[ni][nj][0] == k:
                    temp2.append((ni, nj))

        if temp1:
            ni, nj = temp1[0]
        elif temp2:
            ni, nj = temp2[0]
        if new_arr[ni][nj][0] == 0:
            new_arr[ni][nj] = [k]
        else:
            new_arr[ni][nj].append(k)
        d[k] = d_list.index((ni - i, nj - j))
        sharks[k] = (ni, nj)
    arr = new_arr[::]

    # 제거
    for i in range(N):
        for j in range(N):
            if len(arr[i][j]) != 1:
                arr[i][j].sort()
                dead = arr[i][j][1:]
                arr[i][j] = [arr[i][j][0]]
                for k in dead:
                    sharks[k] = 0
            if v[i][j][1]:
                v[i][j][1] -= 1
                if v[i][j][1] == 0:
                    v[i][j][0] = 0
    t += 1

if t > 1000:
    print(-1)
else:
    print(t)