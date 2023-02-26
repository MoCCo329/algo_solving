# 11689. GCD(n, k) = 1  2023-02-26


from math import sqrt, floor

N = int(input())
END = floor(sqrt(N)) + 1
cur = N
ans = N

for i in range(2, END):
    if cur % i != 0: continue

    ans -= ans // i
    while cur % i == 0:
        cur //= i

if cur > 1:
    ans -= ans // cur

print(ans)