# 2342. Dance Dance Revolution  2023-01-22


import sys
sys.setrecursionlimit(100001)


def step(nex, move, hold):  # 옮기려는 위치, 움직이는 발 위치, 안움직이는 발 위치
    if nex == move: return 1
    elif nex == hold: return INF
    elif move == 0: return 2
    elif abs(nex - move) % 2: return 3
    else: return 4


def get_dp(i, r, l):  # i번째 스탭 r발, l발 위치에서 최솟값 구하기
    if i == L - 1: return 0
    if dp[i][r * 5 + l] == INF:
        dp[i][r * 5 + l] = min(get_dp(i + 1, buttons[i], l) + step(buttons[i], r, l), get_dp(i + 1, r, buttons[i]) + step(buttons[i], l, r))
    return dp[i][r * 5 + l]


buttons = list(map(int, input().split()))
L = len(buttons)
INF = 400000
dp = [[INF] * 25 for _ in range(L)]  # 번호, 오른발, 왼발

print(get_dp(0, 0, 0))