# 14499. 주사위 굴리기 2022-04-10

def move(direc):
    if direc == 3:  # 북
        dice[1] = [dice[1][3]] + dice[1][:3]
    elif direc == 4:  # 남
        dice[1] = dice[1][1:] + [dice[1][0]]
    elif direc == 1:  # 동
        temp1 = dice[0][1]
        temp2 = dice[1][1]
        dice[0][1] = dice[1][3]
        dice[1] = [dice[1][0], temp1, dice[1][2], dice[2][1]]
        dice[2][1] = temp2
    else:  # 서
        temp1 = dice[0][1]
        temp2 = dice[1][3]
        dice[0][1] = dice[1][1]
        dice[1] = [dice[1][0], dice[2][1], dice[1][2], temp1]
        dice[2][1] = temp2


N, M, i, j, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
moves = list(map(int, input().split()))
dice = [[0] * 4 for _ in range(3)]  # 전개도를 왼쪽으로 눕힌 배열
d_list = [0, [0, 1], [0, -1], [-1, 0], [1, 0]]

for d in moves:
    di, dj = d_list[d]
    ni, nj = i + di, j + dj
    if 0 <= ni < N and 0 <= nj < M:
        move(d)
        if arr[ni][nj] == 0:
            arr[ni][nj] = dice[1][1]
        else:
            dice[1][1] = arr[ni][nj]
            arr[ni][nj] = 0
        i, j = ni, nj
        print(dice[1][3])