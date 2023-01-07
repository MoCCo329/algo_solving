# 7579. 앱  2023-01-07


N, M = map(int, input().split())
m_list = list(map(int, input().split()))
c_list = list(map(int, input().split()))

dp = [[0] * (100 * N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    curr_m = m_list[i - 1]
    curr_c = c_list[i - 1]
    for j in range(100 * N + 1):
        if curr_c <= j:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - curr_c] + curr_m)
        else:
            dp[i][j] = dp[i - 1][j]


ans = -1
for j in range(100 * N + 1):
    for i in range(1, N + 1):
        if dp[i][j] >= M:
            ans = j
            break
    if ans != -1:
        break

print(ans)