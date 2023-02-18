# 14438. 수열과 쿼리 17  2023-02-18


N = int(input())
k = 1
while k < N: k <<= 1
st = [1e9 + 1] * (k << 1)
temp = map(int, input().split())
for i in range(k, k + N):
    st[i] = temp.__next__()
for i in range(k - 1, 0, -1):
    st[i] = min(st[i * 2], st[i * 2 + 1])

M = int(input())
for _ in range(M):
    a, b, c = map(int, input().split())
    if a == 1:
        st[k + b - 1] = c
        idx = (k + b - 1) // 2
        while idx > 0:
            st[idx] = min(st[idx * 2], st[idx * 2 + 1])
            idx //= 2
    else:
        ans = 1e9 + 1
        b += k - 1
        c += k - 1
        while b <= c:
            if b % 2 == 1:
                ans = min(ans, st[b])
            if c % 2 == 0:
                ans = min(ans, st[c])
            b = (b + 1) // 2
            c = (c - 1) // 2
        print(ans)