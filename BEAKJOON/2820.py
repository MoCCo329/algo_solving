# 2820. 자동차 공장  2023-06-17


import sys
input = sys.stdin.readline


def apply(idx, v):
    st[idx] += v * size[idx]
    if idx < k:
        lazy[idx] += v


def up(idx):
    while idx > 1:
        idx >>= 1
        st[idx] = st[idx << 1] + st[idx << 1 | 1]


def down(idx):
    for hh in range(h - 1, 0, -1):
        i = idx >> hh
        if lazy[i] != 0:
            st[i << 1] += lazy[i] * size[i << 1]
            st[i << 1 | 1] += lazy[i] * size[i << 1 | 1]
            if (i << 1) < k:
                lazy[i << 1] += lazy[i]
                lazy[i << 1 | 1] += lazy[i]
            lazy[i] = 0


N, M = map(int, input().split())
base = [0] * (N + 1)
c = [[] for _ in range(N + 1)]
base[1] = int(input())
for i in range(2, N + 1):
    a, b = map(int, input().split())
    base[i] = a
    c[b].append(i)
k = 1
h = 1
while k < N:
    k <<= 1
    h += 1
st = [0] * (k << 1)
size = [1] * (k << 1)
lazy = [0] * k

s = [0] * (N + 1)
e = [0] * (N + 1)
cnt = 0
stack = [1]
while stack:
    i = stack.pop()
    if s[i] != 0:
        e[i] = cnt + k - 1
        continue
    stack.append(i)
    cnt += 1
    s[i] = cnt + k - 1
    st[cnt + k - 1] = base[i]
    for j in c[i]:
        stack.append(j)

for i in range(k - 1, 0, - 1):
    st[i] = st[i << 1] + st[i << 1 | 1]
    size[i] = size[i << 1] + size[i << 1 | 1]


for _ in range(M):
    order, *nums = input().split()
    if order == 'p':
        l, r, v = s[int(nums[0])] + 1, e[int(nums[0])], int(nums[1])
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
        if l0 < (k << 1):
            up(l0)
        up(r0)
    else:
        down(s[int(nums[0])])
        print(st[s[int(nums[0])]])