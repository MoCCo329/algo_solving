# 10942. 팰린드롬?  2022-09-04


import sys


N = int(input())
arr = list(map(int, sys.stdin.readline().split()))
dp = [[0] * N for _ in range(N)]
for length in range(N):
    for start in range(N - length):
        end = start + length
        if arr[start] == arr[end]:
            if start + 1 >= end:
                dp[start][end] = 1
            elif dp[start + 1][end - 1]:
                dp[start][end] = 1

M = int(input())
for _ in range(M):
    S, E = map(int, sys.stdin.readline().split())
    if dp[S - 1][E - 1]:
        print(1)
    else:
        print(0)