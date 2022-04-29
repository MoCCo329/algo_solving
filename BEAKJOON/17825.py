# 17825 주사위 윶놀이 G2 2022-04-29


# 코드 중복 없애고 최적화 해야하는데 졸리다. 그렇다고 내일 이어 하기에는 그만한 의미가 없는것 같아 덮어둔다.
# 주사위를 한칸씩 움직이는게 이상한 분기처리가 없어 의외로 빠르게 돌 수 있었다.

def move(k, m, turn):  # k번 말을 m칸 이동한다.
    if p[k][0] == 1:
        next = p[k][1] + m
        if next >= L1:
            p[k] = [-1, -1]
            score = 0
        elif g1[next] == 10:
            if test(2, -1):
                return 0
            p[k] = [2, -1]
            score = 10
        elif g1[next] == 20:
            if test(3, -1):
                return 0
            p[k] = [3, -1]
            score = 20
        elif g1[next] == 30:
            if test(4, -1):
                return 0
            p[k] = [4, -1]
            score = 30
        else:
            if test(1, next):
                return 0
            p[k][1] = next
            score = g1[next]

    elif p[k][0] == 2:
        next = p[k][1] + m
        if next >= L2:
            next -= L2
            if next >= L5:
                next -= L5
                if next == 0:
                    if test(1, 20):
                        return 0
                    p[k] = [1, 20]
                    score = 40
                else:
                    p[k] = [-1, -1]
                    score = 0
            else:
                if test(5, next):
                    return 0
                p[k] = [5, next]
                score = g5[next]
        else:
            if test(2, next):
                return 0
            p[k][1] = next
            score = g2[next]

    elif p[k][0] == 3:
        next = p[k][1] + m
        if next >= L3:
            next -= L3
            if next >= L5:
                next -= L5
                if next == 0:
                    if test(1, 20):
                        return 0
                    p[k] = [1, 20]
                    score = 40
                else:
                    p[k] = [-1, -1]
                    score = 0
            else:
                if test(5, next):
                    return 0
                p[k] = [5, next]
                score = g5[next]
        else:
            if test(3, next):
                return 0
            p[k][1] = next
            score = g3[next]

    elif p[k][0] == 4:
        next = p[k][1] + m
        if next >= L4:
            next -= L4
            if next >= L5:
                next -= L5
                if next == 0:
                    if test(1, 20):
                        return 0
                    p[k] = [1, 20]
                    score = 40
                else:
                    p[k] = [-1, -1]
                    score = 0
            else:
                if test(5, next):
                    return 0
                p[k] = [5, next]
                score = g5[next]
        else:
            if test(4, next):
                return 0
            p[k][1] = next
            score = g4[next]

    else:
        next = p[k][1] + m
        if next >= L5:
            next -= L5
            if next == 0:
                if test(1, 20):
                    return 0
                p[k] = [1, 20]
                score = 40
            else:
                p[k] = [-1, -1]
                score = 0
        else:
            if test(5, next):
                return 0
            p[k][1] = next
            score = g5[next]

    scores[turn] = score
    return 1  # 이동 성공


def test(g, n):  # g번 말판 n번 위에 다른 말이 있는지.
    for i in range(4):
        if p[i] == [g, n]:
            return 1
    return 0


def dfs(turn):
    global ans

    if turn == 10:
        tempAns = sum(scores)
        if ans < tempAns:
            ans = tempAns

    elif (10 - turn) * 40 < ans - sum(scores):
        return

    else:
        for i in range(4):
            temp = [p[i][0], p[i][1]]
            if p[i][0] != -1 and move(i, dices[turn], turn):
                dfs(turn + 1)
                p[i] = temp
                scores[turn] = 0


g1 = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]
g2 = [13, 16, 19]  # 10에서 분기 끝나면 25로
g3 = [22, 24]  # 20에서 분기 끝나면 25로
g4 = [28, 27, 26]  # 30에서 분기 끝나면 25로
g5 = [25, 30, 35]  # 25에서 시작 끝나면 40으로

p = [[1, 0] for _ in range(4)]  # 1번 말판 0번 자리에 위치
scores = [0] * 10
turn = 0
L1 = 21
L2 = 3
L3 = 2
L4 = 3
L5 = 3
dices = list(map(int, input().split()))
v = [0] * 5  # 10, 20, 25, 30, 40에 다른 말이 있는지.

ans = 0
dfs(0)
print(ans)