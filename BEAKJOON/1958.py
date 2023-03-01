# 1958. LCS3  2023-03-01


A = input()
B = input()
C = input()

dp = [[[0] * (len(C) + 1) for _ in range(len(B) + 1)] for _ in range(len(A) + 1)]

for i in range(len(A)):
    for j in range(len(B)):
        for k in range(len(C)):
            dp[i][j][k] = dp[i - 1][j - 1][k - 1] + 1 if A[i] == B[j] == C[k] else max(dp[i - 1][j][k], dp[i][j - 1][k], dp[i][j][k - 1])

print(dp[len(A) - 1][len(B) - 1][len(C) - 1])