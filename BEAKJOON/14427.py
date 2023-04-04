# 14427. 수열과 쿼리 15  2023-04-04


import sys
input = sys.stdin.readline


N = int(input())
k = 1
while k < N: k <<= 1
INF = 100000000001
st = [(0, INF)] * (k << 1)

iter = map(int, input().split())
for i in range(N):
    st[k + i] = (i + 1, next(iter))
for i in range(k - 1, 0, -1):
    if st[i * 2][1] <= st[i * 2 + 1][1]:
        st[i] = (st[i * 2][0], st[i * 2][1])
    else:
        st[i] = (st[i * 2 + 1][0], st[i * 2 + 1][1])

M = int(input())
for _ in range(M):
    line = input().split()
    if line[0] == '2':
        ans = (N, INF)
        s, e = k, k + N - 1
        while s <= e:
            if s % 2 == 1:
                if ans[1] > st[s][1] or (ans[1] == st[s][1] and ans[0] > st[s][0]):
                    ans = (st[s][0], st[s][1])
                s += 1
            if e % 2 == 0:
                if ans[1] > st[e][1] or (ans[1] == st[e][1] and ans[0] > st[e][0]):
                    ans = (st[e][0], st[e][1])
                e -= 1
            s >>= 1
            e >>= 1
        print(ans[0])

    else:
        i = int(line[1])
        n = int(line[2])
        st[k + i - 1] = (i, n)

        i = (k + i - 1) // 2
        while i > 0:
            if st[i * 2][1] <= st[i * 2 + 1][1]:
                st[i] = (st[i * 2][0], st[i * 2][1])
            else:
                st[i] = (st[i * 2 + 1][0], st[i * 2 + 1][1])
            i >>= 1