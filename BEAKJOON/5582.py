# 5582. 공통 부분 문자열 G5 2022-05-15


# P1 = input()
# P2 = input()
# L1 = len(P1)
# L2 = len(P2)
#
# ans = 0
# for i in range(L1):
#     ni = 0
#     tempAns = 0
#     for j in range(1, min(L2 + 1, i + 1)):
#         if P1[i - ni] == P2[-j]:
#             tempAns += 1
#             if ans < tempAns:
#                 ans = tempAns
#                 print(i - ni, - j)
#         else:
#             tempAns = 0
#         ni += 1
#
# print(ans)

P1 = str(input())
P2 = str(input())
L1 = len(P1)
L2 = len(P2)
ans = 0
dp = [[0 for i in range(L2)] for j in range(L1)]

for i in range(L1):
    for j in range(L2):
        if P1[i] == P2[j]:
            if i == 0 or j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > ans:
                    ans = dp[i][j]

print(ans)