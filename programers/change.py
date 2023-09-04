# 거스름돈.  2023-09-04


def solution(N, money):
    ans = [0] * (N + 1)
    ans[0] = 1
    
    for m in money:
        for i in range(m, N + 1):
            ans[i] = (ans[i] + ans[i - m]) % 1000000007

    return ans[N]
