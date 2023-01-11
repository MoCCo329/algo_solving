# 9251. LCS  2023-01-11


A = input()
B = input()
A_L = len(A)
B_L = len(B)

dp = [[0] * A_L for _ in range(B_L)]
if A[0] == B[0]: dp[0][0] = 1
for j in range(1, A_L):
    dp[0][j] = max(dp[0][j - 1], 1 if A[j] == B[0] else 0)
for i in range(1, B_L):
    dp[i][0] = max(dp[i - 1][0], 1 if A[0] == B[i] else 0)

for i in range(1, B_L):
    for j in range(1, A_L):
        if B[i] == A[j]:
            dp[i][j] = max(dp[i - 1][j - 1] + 1, dp[i - 1][j], dp[i][j - 1])
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[B_L - 1][A_L - 1])