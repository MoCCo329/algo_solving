# 2243. 사탕상자  2023-03-02


import sys
input = sys.stdin.readline


def find(a):
    idx = 1
    while True:
        if idx >= k:
            return idx
        if st[idx * 2] >= a:
            idx = idx * 2
        else:
            a -= st[idx * 2]
            idx = idx * 2 + 1


k = 1 << 20
st = [0] * (k << 1)

N = int(input())
for _ in range(N):
    line = input().split()
    if line[0] == '1':
        a = int(line[1])
        idx = find(a)
        print(idx - k - 1)
        st[idx] -= 1
        idx //= 2
        while idx > 0:
            st[idx] = st[idx * 2] + st[idx * 2 + 1]
            idx //= 2

    else:
        a, b = int(line[1]), int(line[2])
        st[k + a + 1] += b
        idx = (k + a + 1) // 2
        while idx > 0:
            st[idx] = st[idx * 2] + st[idx * 2 + 1]
            idx //= 2