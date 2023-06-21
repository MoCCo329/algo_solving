# 2673. 교차하지 않는 원의 현들의 최대집합  2023-06-21


N = int(input())
adj_matrix = [[0] * 100 for _ in range(100)]
for _ in range(N):
    a, b = map(int, input().split())
    adj_matrix[a - 1][b - 1] = 1
    adj_matrix[b - 1][a - 1] = 1

dp = [[0] * 100 for _ in range(100)]
for j in range(100):
    for i in range(j - 1, -1, -1):
        for k in range(i, j):
            dp[i][j] = max(dp[i][j], dp[i][k] + dp[k + 1][j] + adj_matrix[i][j])

print(dp[0][99])