# 17353. 하늘에서 떨어지는 1, 2, ..., R-L+1개의 별  2023-06-14


import sys
input = sys.stdin.readline


def update_query(now, l, r, s, e, v):
    if lazy[now] != 0:
        st[now] += lazy[now] * size[now]
        if l != r:
            lazy[now << 1] += lazy[now]
            lazy[now << 1 | 1] += lazy[now]
        lazy[now] = 0

    if r < s or e < l:
        return
    if s <= l and r <= e:
        st[now] += v * size[now]
        if l != r:
            lazy[now << 1] += v
            lazy[now << 1 | 1] += v
    else:
        m = (l + r) // 2
        update_query(now << 1, l, m, s, e, v)
        update_query(now << 1 | 1, m + 1, r, s, e, v)
        st[now] = st[now << 1] + st[now << 1 | 1]


def get_query(now, l, r, s, e):
    if lazy[now] != 0:
        st[now] += lazy[now] * size[now]
        if l != r:
            lazy[now << 1] += lazy[now]
            lazy[now << 1 | 1] += lazy[now]
        lazy[now] = 0

    if r < s or e < l:
        return 0
    if s <= l and r <= e:
        return st[now]
    else:
        m = (l + r) // 2
        return get_query(now << 1, l, m, s, e) + get_query(now << 1 | 1, m + 1, r, s, e)


N = int(input())
k = 1
h = 1
while k < N:
    k <<= 1
    h += 1
st = [0] * (k << 1)
lazy = [0] * (k << 1)
size = [0] * (k << 1)
arr = list(map(int, input().split()))
st[k] = arr[0]
for i in range(1, N):
    st[k + i] = arr[i] - arr[i - 1]
for i in range(k):
    size[k + i] = 1
for i in range(k - 1, 0, -1):
    st[i] = st[i << 1] + st[i << 1 | 1]
    size[i] = size[i << 1] + size[i << 1 | 1]

for _ in range(int(input())):
    order, *nums = map(int, input().split())
    if order == 1:
        update_query(1, 1, k, nums[0], nums[1], 1)
        update_query(1, 1, k, nums[1] + 1, nums[1] + 1, -(nums[1] - nums[0] + 1))
    else:
        print(get_query(1, 1, k, 1, nums[0]))