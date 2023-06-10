# 1395. 스위치  2023-06-10


import sys
input = sys.stdin.readline


def getQuery(now, l, r, s, e):
    if r < s or e < l: return 0
    if l == r: return st[now]

    if lazy[now]:
        st[now] = (r - l + 1) - st[now]
        if (r - l + 1) == 2:
            st[now << 1] ^= 1
            st[now << 1 | 1] ^= 1
        else:
            lazy[now << 1] = not lazy[now << 1]
            lazy[now << 1 | 1] = not lazy[now << 1 | 1]
        lazy[now] = False

    if s <= l and r <= e: return st[now]
    m = (l + r) // 2
    return getQuery(now << 1, l, m, s, e) + getQuery(now << 1 | 1, m + 1, r, s, e)


def updateQuery(now, l, r, s, e):
    if l != r and (lazy[now] ^ (s <= l and r <= e)):
        st[now] = (r - l + 1) - st[now]
        if (r - l + 1) == 2:
            st[now << 1] ^= 1
            st[now << 1 | 1] ^= 1
        else:
            lazy[now << 1] = not lazy[now << 1]
            lazy[now << 1 | 1] = not lazy[now << 1 | 1]
        lazy[now] = False

    if r < s or e < l: return
    if l == r: st[now] ^= 1
    elif s <= l and r <= e:
        lazy[now] = False
    else:
        m = (l + r) // 2
        updateQuery(now << 1, l, m, s, e)
        updateQuery(now << 1 | 1, m + 1, r, s, e)
        st[now] = st[now << 1] + st[now << 1 | 1]


N, M = map(int, input().split())
k = 1
while k < N: k <<= 1
st = [0] * (k << 1)
lazy = [False] * k

for _ in range(M):
    a, b, c = map(int, input().split())
    if a == 0:
        updateQuery(1, 1, k, b, c)
    else:
        print(getQuery(1, 1, k, b, c))