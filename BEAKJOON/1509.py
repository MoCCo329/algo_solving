# 1509. 팰린드롬 분할  2023-05-22


s = input()
L = len(s)
dp = [i for i in range(L + 1)]
arr_odd = [0] * L
arr_even = [0] * L

for i in range(L):
    cnt = 1
    for j in range(1, L):
        if i - j < 0 or i + j >= L: break
        if s[i - j] == s[i + j]: cnt += 1
        else: break
    arr_odd[i] = cnt

    cnt = 0
    for j in range(L):
        if i - j < 0 or i + 1 + j >= L: break
        if s[i - j] == s[i + 1 + j]: cnt += 1
        else: break
    arr_even[i] = cnt

for i in range(1, L + 1):
    for j in range(1, arr_odd[i - 1] + 1):
        if 0 <= i - j and i + j - 1 <= L:
            dp[i + j - 1] = min(dp[i + j - 1], dp[i - j] + 1)
    for j in range(1, arr_even[i - 1] + 1):
        if 0 <= i - j and i + j <= L:
            dp[i + j] = min(dp[i + j], dp[i - j] + 1)

print(dp[L])