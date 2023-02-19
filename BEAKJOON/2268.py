# 2268. 수들의 합 7  2023-02-19


import sys
input = sys.stdin.readline


N, M = map(int, input().split())
k = 1
while k < N: k <<= 1
st = [0] * (k << 1)

for _ in range(M):
    a, b, c = map(int, input().split())
    if a == 0:
        ans = 0
        if b > c: b, c = c, b
        b += k - 1
        c += k - 1
        while b <= c:
            if b % 2 == 1:
                ans += st[b]
                b += 1
            if c % 2 == 0:
                ans += st[c]
                c -= 1
            b //= 2
            c //= 2
        print(ans)
    else:
        idx = k + b - 1
        gap = c - st[idx]
        while idx > 0:
            st[idx] += gap
            idx //= 2