# 14891. 톱니바퀴 2022-04-16

def turn(i, dire):
    if dire == 1:
        gears[i] = [gears[i][7]] + gears[i][:7]
    else:
        gears[i] = gears[i][1:8] + [gears[i][0]]


gears = [list(map(int, input())) for _ in range(4)]
K = int(input())
for _ in range(K):
    i, dire = map(int, input().split())
    i -= 1

    k = 0
    while True:
        if i + k + 1 < 4:
            if gears[i + k][2] != gears[i + k + 1][6]:
                k += 1
            else: break
        else: break
    for l in range(k):
        turn(i + l + 1, -dire * (-1) ** l)

    k = 0
    while True:
        if i - k - 1 >= 0:
            if gears[i - k][6] != gears[i - k - 1][2]:
                k += 1
            else: break
        else: break
    for l in range(k):
        turn(i - l - 1, -dire * (-1) ** l)
    turn(i, dire)

print(sum([gears[i][0] * (1 << i) for i in range(4)]))