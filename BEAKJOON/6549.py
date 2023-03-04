# 6549. 히스토그램에서 가장 큰 직사각형  2023-03-05


import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline


def divide(s, e):
    global ans
    if s > e: return
    if s == e:
        ans = max(ans, st[s][0])
        return

    partition = getMin(s, e)
    ans = max(ans, (e - s + 1) * partition[0])

    divide(s, partition[1] - 1)
    divide(partition[1] + 1, e)


def getMin(s, e):
    temp = (1e9, -1)
    while s <= e:
        if s % 2 == 1:
            temp = temp if temp[0] < st[s][0] else st[s]
            s += 1
        if e % 2 == 0:
            temp = temp if temp[0] < st[e][0] else st[e]
            e -= 1
        s >>= 1
        e >>= 1

    return temp


while True:
    iterator = map(int, input().split())
    N = next(iterator)
    if N == 0: break

    k = 1
    while k < N: k <<= 1
    st = [(1e9, -1)] * (k << 1)
    for i in range(N): st[k + i] = (next(iterator), k + i)
    for i in range(k - 1, 0, -1): st[i] = st[i * 2] if st[i * 2][0] <= st[i * 2 + 1][0] else st[i * 2 + 1]

    ans = 0
    divide(k, k + N - 1)
    print(ans)