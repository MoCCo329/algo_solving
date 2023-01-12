# 17404. RGB거리 2  2023-01-12


N = int(input())
lights = [tuple(map(int, input().split())) for _ in range(N)]
dp = [[0] * 3 for _ in range(N)]

ans = 1000001
for color in range(3):

    for j in range(3):
        if j == color:
            dp[0][j] = lights[0][j]
        else:
            dp[0][j] = 1000001

    for i in range(1, N):
        dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + lights[i][0]
        dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + lights[i][1]
        dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + lights[i][2]

    for j in range(3):
        if j == color: continue

        ans = min(ans, dp[N - 1][j])

print(ans)