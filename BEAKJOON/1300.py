# 1300. k번째 수  2023-02-25


def count(n):
    temp = 0

    for i in range(1, N + 1):
        temp += min(n // i, N)

    return temp


N = int(input())
K = int(input())
ans = 0

l, r = 1, K
while l <= r:
    m = (l + r) // 2

    if count(m) >= K:
        r = m - 1
    else:
        l = m + 1

print(l)