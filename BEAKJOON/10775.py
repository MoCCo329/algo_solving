# 10775. 공항  2022-08-04


def find(x):
    if uf[x] == x:
        return x
    uf[x] = find(uf[x])
    return uf[x]

G = int(input())
P = int(input())
arr = []
for _ in range(P):
    arr.append(int(input()))

uf = [i for i in range(G + 1)]
ans = 0
for p in arr:
    g = find(p)
    if g == 0:
        break
    uf[g] = uf[g - 1]
    ans += 1
print(ans)