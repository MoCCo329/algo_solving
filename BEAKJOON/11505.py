# 11505. 구간 곱 구하기 2023-02-08


N, M, K = map(int, input().split())
k = 1
while k < N: k <<= 1
st = [1] * (k << 1)

for i in range(N):
    st[i + k] = int(input())

for i in range(k - 1, 0, -1):
    st[i] = st[i * 2] * st[i * 2 + 1] % 1000000007

for _ in range(M + K):
    a, b, c = map(int, input().split())
    if a == 1:
        st[b + k - 1] = c
        i = (b + k - 1) // 2
        while i > 0:
            st[i] = st[i * 2] * st[i * 2 + 1] % 1000000007
            i //= 2
    else:
        tot = 1
        b += k - 1
        c += k - 1
        while b <= c:
            if b % 2 == 1: tot = tot * st[b] % 1000000007
            if c % 2 == 0: tot = tot * st[c] % 1000000007
            b = (b + 1) // 2
            c = (c - 1) // 2
        print(tot)