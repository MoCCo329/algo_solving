# 7578. 공장  2023-03-12


import sys
input = sys.stdin.readline


N = int(input())
arr = list(map(int, input().split()))
iterator = map(int, input().split())
hashMap = {next(iterator) : i for i in range(N)}

k = 1
while k < N: k <<= 1
st = [0] * (k << 1)
ans = 0

for i in range(N):
    j = hashMap[arr[i]]

    temp = 0
    s, e = k, k + j
    while s <= e:
        if s % 2 == 1:
            temp += st[s]
            s += 1
        if e % 2 == 0:
            temp += st[e]
            e -= 1
        s, e = s // 2, e // 2

    st[k + j] = 1
    idx = (k + j) // 2
    while idx > 0:
        st[idx] = st[idx * 2] + st[idx * 2 + 1]
        idx //= 2

    ans += i - temp

print(ans)