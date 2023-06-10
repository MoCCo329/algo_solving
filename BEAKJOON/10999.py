# 10999. 구간 합 구하기 2  2023-06-10


import sys
input = sys.stdin.readline


def getQuery(now, l, r, s, e):
    if r < s or e < l: return 0

    if l != r and lazy[now] != 0:
        st[now] += (r - l + 1) * lazy[now]
        if (r - l + 1) == 2:
            st[now << 1] += lazy[now]
            st[now << 1 | 1] += lazy[now]
        else:
            lazy[now << 1] += lazy[now]
            lazy[now << 1 | 1] += lazy[now]
        lazy[now] = 0

    if l == r: return st[now]
    if s <= l and r <= e: return st[now]
    m = (l + r) >> 1
    return getQuery(now << 1, l, m, s, e) + getQuery(now << 1 | 1, m + 1, r, s, e)


def updateQuery(now, v, l, r, s, e):
    if l != r and lazy[now] != 0:
        st[now] += (r - l + 1) * lazy[now]
        if (r - l + 1) == 2:
            st[now << 1] += lazy[now]
            st[now << 1 | 1] += lazy[now]
        else:
            lazy[now << 1] += lazy[now]
            lazy[now << 1 | 1] += lazy[now]
        lazy[now] = 0

    if r < s or e < l: return
    if l == r:
        st[now] += v
        return
    if s <= l and r <= e:
        st[now] += (r - l + 1) * v
        if (r - l + 1) == 2:
            st[now << 1] += v
            st[now << 1 | 1] += v
        else:
            lazy[now << 1] += v
            lazy[now << 1 | 1] += v
        return
    else:
        m = (l + r) >> 1
        updateQuery(now << 1, v, l, m, s, e)
        updateQuery(now << 1 | 1, v, m + 1, r, s, e)
        st[now] = st[now << 1] + st[now << 1 | 1]


N, M, K = map(int, input().split())
k = 1
while k < N: k <<= 1
st = [0] * (k << 1)
lazy = [0] * k
for i in range(N):
    st[k + i] = int(input())
for i in range(k - 1, 0, -1):
    st[i] = st[i << 1] + st[i << 1 | 1]

for _ in range(M + K):
    order, *nums = map(int, input().split())
    if order == 1:
        updateQuery(1, nums[2], 1, k, nums[0], nums[1])
    else:
        print(getQuery(1, 1, k, nums[0], nums[1]))