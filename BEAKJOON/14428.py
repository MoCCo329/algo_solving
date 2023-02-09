# 14428. 수열과 쿼리 16  2023-02-09


N = int(input())
k = 1
while k < N: k <<= 1
iterator = map(int, input().split())
st = [(1000000000, 100000) for _ in range(k)] + list((iterator.__next__(), i) for i in range(1, N + 1)) + [(1000000000, 100000) for _ in range(k - N)]
for i in range(k - 1, 0, -1):
    st[i] = st[i * 2] if st[i * 2][0] <= st[i * 2 + 1][0] else st[i * 2 + 1]

M = int(input())
for _ in range(M):
    a, b, c = map(int, input().split())
    if a == 1:
        st[b + k - 1] = (c, b)
        i = (b + k - 1) // 2
        while i > 0:
            st[i] = st[i * 2] if st[i * 2][0] <= st[i * 2 + 1][0] else st[i * 2 + 1]
            i //= 2
    else:
        ans = (1000000000, 100000)
        b += k - 1
        c += k - 1
        while b <= c:
            if b & 1 and ans[0] >= st[b][0]:
                if ans[0] > st[b][0] or ans[1] > st[b][1]:
                    ans = st[b]
            if not c & 1 and ans[0] >= st[c][0]:
                if ans[0] > st[c][0] or ans[1] > st[c][1]:
                    ans = st[c]
            b = (b + 1) // 2
            c = (c - 1) // 2
        print(ans[1])