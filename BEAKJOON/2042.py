# 2042. 구간 합 구하기  2023-02-10


def query(s, e):
    tot = 0

    s = s - 1 + k
    e = e - 1 + k
    while s <= e:
        if s % 2 == 1: tot += st[s]
        if e % 2 == 0: tot += st[e]
        s = (s + 1) // 2
        e = (e - 1) // 2

    print(tot)


def update(i, n):
    i = i - 1 + k
    st[i] = n

    i >>= 1
    while i > 0:
        st[i] = st[i * 2] + st[i * 2 + 1]
        i >>= 1


N, M, K = map(int, input().split())
k = 1
while k < N: k <<= 1
st = [0] * (k << 1)
for i in range(N):
    st[k + i] = int(input())
for i in range(k - 1, 0, -1):
    st[i] = st[i * 2] + st[i * 2 + 1]

for _ in range(M + K):
    a, b, c = map(int, input().split())
    if a == 1:
        update(b, c)
    else:
        query(b, c)