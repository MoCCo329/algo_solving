# 2629. 양팔저울  2023-01-20


N = int(input())
w_list = list(map(int, input().split()))
M = int(input())
m_list = list(map(int, input().split()))

MAX = 40001
dp = [[0] * MAX for _ in range(N)]

dp[0][w_list[0]] = 1
for i in range(1, N):
    w = w_list[i]
    dp[i][w] = 1
    for j in range(40001):
        if dp[i - 1][j]:
            dp[i][j] = 1
            dp[i][max(w - j, j - w)] = 1
            if j + w < MAX:
                dp[i][j + w] = 1

for m in m_list:
    print("Y" if dp[-1][m] else "N", end=" ")
