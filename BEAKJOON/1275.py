# 1275. 커피숍2  2023-02-10


import sys
input = sys.stdin.readline


N, Q = map(int, input().split())
MAX_V = 2 << 31
k = 1
while k < N: k <<= 1
st = [0] * k + list(map(int, input().split())) + [0] * (k - N)
for i in range(k - 1, 0, -1):
    st[i] = st[i * 2] + st[i * 2 + 1]

for _ in range(Q):
    x, y, a, b = map(int, input().split())

    tot = 0
    if x > y: x, y = y, x
    x += k - 1
    y += k - 1
    while x <= y:
        if x & 1: tot += st[x]
        if not y & 1: tot += st[y]
        x = (x + 1) // 2
        y = (y - 1) // 2
    print(tot)

    st[a + k - 1] = b
    i = (a + k - 1) // 2
    while i > 0:
        st[i] = st[i * 2] + st[i * 2 + 1]
        i >>= 1
