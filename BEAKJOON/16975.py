# 16975. 수열과 쿼리 21  2023-06-14


import sys
input = sys.stdin.readline


def update_query(now, l, r, s, e, v):
    if l != r and lazy[now] != 0:
        if r - l + 1 == 2:
            t[(now << 1) - k] += lazy[now]
            t[(now << 1 | 1) - k] += lazy[now]
        else:
            lazy[now << 1] += lazy[now]
            lazy[now << 1 | 1] += lazy[now]
        lazy[now] = 0

    if r < s or e < l:
        return
    if l == r:
        t[now - k] += v
        return
    elif s <= l and r <= e:
        if r - l + 1 == 2:
            t[(now << 1) - k] += v
            t[(now << 1 | 1) - k] += v
        else:
            lazy[now << 1] += v
            lazy[now << 1 | 1] += v
    else:
        m = (l + r) // 2
        update_query(now << 1, l, m, s, e, v)
        update_query(now << 1 | 1, m + 1, r, s, e, v)


def get_qeury(now, l, r, s, e):
    if r < s or e < l: return 0
    if l == r: return t[now - k]

    if lazy[now] != 0:
        if r - l + 1 == 2:
            t[(now << 1) - k] += lazy[now]
            t[(now << 1 | 1) - k] += lazy[now]
        else:
            lazy[now << 1] += lazy[now]
            lazy[now << 1 | 1] += lazy[now]
        lazy[now] = 0

    m = (l + r) // 2
    return get_qeury(now << 1, l, m, s, e) + get_qeury(now << 1 | 1, m + 1, r, s, e)


N = int(input())
k = 1
while k < N: k <<= 1
t = list(map(int, input().split()))
lazy = [0] * k

for _ in range(int(input())):
    order, *nums = map(int, input().split())
    if order == 1:
        update_query(1, 1, k, nums[0], nums[1], nums[2])
    else:
        print(get_qeury(1, 1, k, nums[0], nums[0]))