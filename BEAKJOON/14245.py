# 14245. XOR  2023-06-15


import sys
input = sys.stdin.readline


def apply(idx, v):
    if idx < k:
        lazy[idx] ^= v
    else:
        st[idx] ^= v


def up(idx):
    while idx > 1:
        idx >>= 1
        st[idx] = st[idx << 1] ^ st[idx << 1 | 1]


def down(idx):
    for i in range(h - 1, 0, -1):
        j = idx >> i
        if lazy[j] != 0:
            apply(j << 1, lazy[j])
            apply(j << 1 | 1, lazy[j])
            lazy[j] = 0


def update_query(l, r, v):
    l += k
    r += k
    l0, r0 = l, r
    while l <= r:
        if l & 1 == 1:
            apply(l, v)
            l += 1
        if r & 1 == 0:
            apply(r, v)
            r -= 1
        l >>= 1
        r >>= 1
    up(l0)
    up(r0)


def get_query(l, r):
    l += k
    r += k
    down(l)
    down(r)
    ans = 0
    while l <= r:
        if l & 1 == 1:
            ans ^= st[l]
            l += 1
        if r & 1 == 0:
            ans ^= st[r]
            r -= 1
        l >>= 1
        r >>= 1
    return ans


N = int(input())
k = 1
h = 1
while k < N:
    k <<= 1
    h += 1
st = [0] * (k << 1)
iterator = map(int, input().split())
for i in range(N):
    st[i + k] = next(iterator)
for i in range(k - 1, 0, -1):
    st[i] = st[i << 1] ^ st[i << 1 | 1]
lazy = [0] * k

for _ in range(int(input())):
    order, *nums = map(int, input().split())
    if order == 1:
        update_query(nums[0], nums[1], nums[2])
    else:
        print(get_query(nums[0], nums[0]))