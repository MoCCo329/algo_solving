# 13459. 구슬 탈출 2022-06-03

d_list = [[-1, 0], [1, 0], [0, -1], [0, 1]]
def dfs(cnt, D):
    global ans
    chk = 0
    if cnt == 10 or cnt >= ans:
        return
    else:
        for d in range(4):
            if d // 2 == D // 2:
                continue
            # 움직인 후 위치 찾기
            di, dj = d_list[d]
            balls.sort(key=lambda x: (x[d // 2]), reverse=(d % 2))
            temp = [balls[i][::] for i in range(2)]
            for k in range(2):
                i, j = balls[k][:2]
                arr[i][j] = "."
                while True:
                    ni = i + di
                    nj = j + dj
                    if arr[ni][nj] == ".":
                        i, j = ni, nj
                    elif arr[ni][nj] == "O":
                        if balls[k][2] == "R":
                            if chk != -1:
                                chk = 1
                            break
                        else:
                            chk = -1
                            break
                    else:
                        arr[i][j] = balls[k][2][::]
                        balls[k][0], balls[k][1] = i, j
                        break

            if chk == 0:
                dfs(cnt + 1, d)

            # 배열 원상복구
            for i in range(2):
                arr[balls[i][0]][balls[i][1]] = "."
                balls[i] = temp[i][::]
                arr[temp[i][0]][temp[i][1]] = temp[i][2][::]

            if chk == 1:
                ans = cnt + 1
                return
            elif chk == -1:
                chk = 0


N, M = map(int, input().split())
arr = [list(map(str, input())) for _ in range(N)]
balls = [0, 0]
for i in range(N):
    for j in range(M):
        if arr[i][j] == "R":
            balls[0] = [i, j, "R"]
        elif arr[i][j] == 'B':
            balls[1] = [i, j, "B"]

ans = 11
dfs(0, 4)
if ans != 11:
    print(1)
else:
    print(0)