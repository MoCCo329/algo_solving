# 연속 펄스 부분 수열의 합  2023-04-14


def solution(arr):
    N = len(arr)
    arr = [arr[i] * (-1) ** i for i in range(N)]
    
    dp, dp_rev = [0] * N, [0] * N
    dp[0], dp_rev[0] = arr[0], arr[0]
    
    for i in range(1, N):
        dp[i] = max(dp[i - 1] + arr[i], arr[i])
        dp_rev[i] = min(dp_rev[i - 1] + arr[i], arr[i])

    return max(max(dp), -min(dp_rev))