# 2517. 달리기  2023-06-18


import sys
input = sys.stdin.readline


def get_query(n):
    temp = 0
    n += 1
    while n > 0:
        temp += fwt[n]
        n &= n - 1
    return temp


def update_query(n):
    n += 1
    while n < cnt + 1:
        fwt[n] += 1
        n += n & -n


N = int(input())
arr = list(int(input()) for _ in range(N))
sorted_arr = sorted(arr)
num_to_idx = {}
cnt = 0
for num in sorted_arr:
    if num in num_to_idx:
        continue
    cnt += 1
    num_to_idx[num] = cnt

fwt = [0] * (cnt + 1)
ans = [0] * N
for idx in range(N):
    n = arr[idx]
    n = num_to_idx[n]
    poss = get_query(n - 1)
    ans[idx] = max(1, idx + 1 - poss)
    update_query(n)

print(*ans, sep="\n")