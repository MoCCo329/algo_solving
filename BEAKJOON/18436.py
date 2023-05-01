# 18436. 수열과 쿼리 37  2023-05-01


import sys
input = sys.stdin.readline

N = int(input())
temp = map(int, input().split())

k = 1
while k <= N: k <<= 1
even_st = [0] * (k << 1)
for i in range(N):
    even_st[k + i] = 1 if next(temp) % 2 == 0 else 0

for idx in range(k - 1, 0, -1):
    even_st[idx] = even_st[idx * 2] + even_st[idx * 2 + 1]

M = int(input())
for _ in range(M):
    a, b, c = map(int, input().split())
    if a == 1:
        idx = k + b - 1
        num = 1 if c % 2 == 0 else 0
        if even_st[idx] == num: continue

        even_st[idx] = num
        while idx > 1:
            idx >>= 1
            even_st[idx] = even_st[idx * 2] + even_st[idx * 2 + 1]
        continue

    tot = 0
    l, r = k + b - 1, k + c - 1

    while l <= r:
        if l % 2 == 1:
            tot += even_st[l]
            l += 1
        if r % 2 == 0:
            tot += even_st[r]
            r -= 1

        l >>= 1
        r >>= 1

    print(tot if a == 2 else c - b + 1 - tot)