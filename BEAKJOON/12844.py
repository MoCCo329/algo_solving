# 12844. XOR  2023-06-11


import sys
input = sys.stdin.readline


def getQuery(now, l, r, s, e):
    if r < s or e < l: return 0
    if l == r: return st[now]

    if lazy[now] != 0:
        if (r - l + 1) == 2:
            st[now << 1] ^= lazy[now]
            st[now << 1 | 1] ^= lazy[now]
        else:
            lazy[now << 1] ^= lazy[now]
            lazy[now << 1 | 1] ^= lazy[now]
        lazy[now] = 0

    if s <= l and r <= e:
        return st[now]
    else:
        m = (l + r) // 2
        return getQuery(now << 1, l, m, s, e) ^ getQuery(now << 1 | 1, m + 1, r, s, e)


def updateQuery(now, l, r, s, e, v):
    if l != r and lazy[now] != 0:
        if (r - l + 1) == 2:
            st[now << 1] ^= lazy[now]
            st[now << 1 | 1] ^= lazy[now]
        else:
            lazy[now << 1] ^= lazy[now]
            lazy[now << 1 | 1] ^= lazy[now]
        lazy[now] = 0

    if r < s or e < l: return
    if l == r: st[now] ^= v
    elif s <= l and r <= e:
        if (r - l + 1) == 2:
            st[now << 1] ^= v
            st[now << 1 | 1] ^= v
        else:
            lazy[now << 1] ^= v
            lazy[now << 1 | 1] ^= v
    else:
        m = (l + r) // 2
        updateQuery(now << 1, l, m, s, e, v)
        updateQuery(now << 1 | 1, m + 1, r, s, e, v)
        st[now] = st[now << 1] ^ st[now << 1 | 1]


N = int(input())
k = 1
while k < N: k <<= 1
st = [0] * (k << 1)
lazy = [0] * k
iterator = map(int, input().split())
for i in range(N):
    st[k + i] = next(iterator)
for i in range(k - 1, 0, -1):
    st[i] = st[i << 1] ^ st[i << 1 | 1]

for _ in range(int(input())):
    order, *nums = map(int, input().split())
    if order == 1:
        updateQuery(1, 0, k - 1, nums[0], nums[1], nums[2])
    else:
        print(getQuery(1, 0, k - 1, nums[0], nums[1]))