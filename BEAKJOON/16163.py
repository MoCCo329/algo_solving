# 16163. #15164번_제보  2023-05-27


S = " ".join(input().strip())
L = len(S)
dp = [1] * L
k, r, p = 0, 0, 0

for i in range(L):
    if i <= r:
        k = min(dp[2 * p - i], r - i)
    else:
        k = 1

    while i + k < L and S[i - k] == S[i + k]:
        k += 1

    if r < i + k:
        r = i + k
        p = i
    dp[i] = k

ans = 0
for i in range(L):
    if i % 2 == 0:
        ans += (dp[i] + 1) // 2
    else:
        ans += dp[i] // 2
print(ans)