# 16474. 이상한 전깃줄  2023-06-28


import sys
input = sys.stdin.readline


def lower_bound(n):
    l, r = 0, len(arr)
    while l < r:
        m = (l + r) // 2
        if arr[m] < n:
            l = m + 1
        else:
            r = m

    return r


N, M = map(int, input().split())
n_dict = {}
m_dict = {}
iterator = map(int, input().split())
for i in range(N):
    n_dict[next(iterator)] = i
iterator = map(int, input().split())
for i in range(M):
    m_dict[next(iterator)] = i

k = int(input())
q = [[] for _ in range(M)]
for _ in range(k):
    n, m = map(int, input().split())
    q[m_dict[m]].append(n_dict[n])

arr = []
for i in range(M):
    if len(q[i]) == 0: continue
    temp = [(n, lower_bound(n)) for n in q[i]]
    for n, idx in temp:
        if idx == len(arr):
            arr.append(n)
        else:
            arr[idx] = min(arr[idx], n)

print(k - len(arr))