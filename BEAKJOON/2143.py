# 2143. 두 배열의 합  2023-05-24


import sys
input = sys.stdin.readline


T = int(input())
N = int(input()) + 1
n_list = [0] + list(map(int, input().split()))
M = int(input()) + 1
m_list = [0] + list(map(int, input().split()))
ans = 0

for i in range(1, N):
    n_list[i] += n_list[i - 1]
for i in range(1, M):
    m_list[i] += m_list[i - 1]

m_sum = {}
for k in range(1, M):
    for l in range(M - k):
        tot = m_list[l + k] - m_list[l]
        if not tot in m_sum: m_sum[tot] = 1
        else: m_sum[tot] += 1

for k in range(1, N):
    for l in range(N - k):
        tot = n_list[l + k] - n_list[l]

        if T - tot in m_sum:
            ans += m_sum[T - tot]

print(ans)