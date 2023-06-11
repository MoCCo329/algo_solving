# 13537. 수열과 쿼리 1  2023-06-12


import sys
input = sys.stdin.readline


def upper_bound(v, arr):
    l, r = 0, len(arr) - 1
    while l <= r:
        m = (l + r) // 2
        if arr[m] <= v:
            l = m + 1
        else:
            r = m - 1

    return l


N = int(input())
k = 1
while k < N: k <<= 1
st = [[] for _ in range(k << 1)]
iterator = map(int, input().split())
for i in range(N):
    st[k + i].append(next(iterator))

for idx in range(k - 1, 0, -1):
    a, b = st[idx << 1], st[idx << 1 | 1]
    i, j = 0, 0
    i_l, j_l = len(a), len(b)

    while i < i_l and j < j_l:
        if a[i] < b[j]:
            st[idx].append(a[i])
            i += 1
        else:
            st[idx].append(b[j])
            j += 1

    while i < i_l:
        st[idx].append(a[i])
        i += 1
    while j < j_l:
        st[idx].append(b[j])
        j += 1

for _ in range(int(input())):
    i, j, v = map(int, input().split())
    i += k - 1
    j += k - 1

    ans = 0
    while i <= j:
        if i % 2 == 1:
            ans += len(st[i]) - upper_bound(v, st[i])
            i += 1
        if j % 2 == 0:
            ans += len(st[j]) - upper_bound(v, st[j])
            j -= 1
        i >>= 1
        j >>= 1

    print(ans)