# 11049. 행렬 곱셈 순서  2023-01-08


N = int(input())
nodes = [tuple(map(int, input().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]

for i in range(N - 1):
    dp[i][i + 1] = nodes[i][0] * nodes[i][1] * nodes[i + 1][1]

for k in range(2, N):
    for i in range(N - k):
        j = i + k

        dp[i][j] = 1 << 32
        for l in range(i, j):
            dp[i][j] = min(dp[i][j], dp[i][l] + dp[l + 1][j] + nodes[i][0] * nodes[l][1] * nodes[j][1])

print(dp[0][N - 1])