# 10775. 공항  2022-08-04


def dfs(k):
    global ans, MAX

    ans = max(ans, sum(v))

    if k == MAX:
        return

    chk = 0
    for i in range(1, arr[k] + 1):
        if v[i]:
            continue
        v[i] = 1
        chk = 1
        dfs(k + 1)
        v[i] = 0
    else:
        if chk == 0:
            MAX = k
            return
    dfs(k + 1)


G = int(input())
P = int(input())
arr = []
for _ in range(P):
    arr.append(int(input()))

v = [0] * (G + 1)
ans = 0
MAX = P
dfs(0)
print(ans)