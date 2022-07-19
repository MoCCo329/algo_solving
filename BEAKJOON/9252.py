# 9252. LCS2  2022-07-19


arr1 = list(input())
arr2 = list(input())
L1 = len(arr1) + 1
L2 = len(arr2) + 1
dp = [[''] * L2 for _ in range(L1)]

for i in range(1, L1):
    for j in range(1, L2):
        if arr1[i - 1] == arr2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + arr1[i - 1]
        else:
            if len(dp[i - 1][j]) > len(dp[i][j - 1]):
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i][j - 1]

ans = dp[-1][-1]
if len(ans) == 0:
    print(0)
else:
    print(len(ans))
    print(ans)