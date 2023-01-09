# 12865. 평범한 배낭  2023-01-09


# N, K = map(int, input().split())
# items = [tuple(map(int, input().split())) for _ in range(N)]
# dp = [[0] * (K + 1) for _ in range(N + 1)]
#
# for i in range(1, N + 1):
#     for j in range(K + 1):
#         cur_w = items[i - 1][0]
#         cur_v = items[i - 1][1]
#
#         if j >= cur_w:
#             dp[i][j] = max(dp[i - 1][j - cur_w] + cur_v, dp[i - 1][j])
#         else:
#             dp[i][j] = dp[i - 1][j]
#
# print(dp[N][K])


N, K = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(N)]
dp = [0] * (K + 1)

items.sort()
for w, v in items:
    for i in range(K, w - 1, -1):
        dp[i] = max(dp[i - w] + v, dp[i])

print(dp[-1])