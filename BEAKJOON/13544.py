# 13544. 수열과 쿼리 3  2023-06-13


import sys
input = sys.stdin.readline


def upper_bound(arr, v):
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
    st[i + k].append(next(iterator))

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

last_ans = 0
for _ in range(int(input())):
    a, b, c = map(int, input().split())
    a = (a ^ last_ans) + k - 1
    b = (b ^ last_ans) + k - 1
    c ^= last_ans

    ans = 0
    while a <= b:
        if a % 2 == 1:
            ans += len(st[a]) - upper_bound(st[a], c)
            a += 1
        if b % 2 == 0:
            ans += len(st[b]) - upper_bound(st[b], c)
            b -= 1
        a >>= 1
        b >>= 1

    print(ans)
    last_ans = ans