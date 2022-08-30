# 20040. 사이클 게임  2022-08-30


def find(a):
    if uf[a] == a:
        return a
    uf[a] = find(uf[a])
    return uf[a]


def union(a, b):  # b의 자식에 a추가
    global ans

    a, b = find(a), find(b)
    if a != b:
        uf[max(a, b)] = min(a, b)
    else:
        ans = turn


N, K = map(int, input().split())
uf = [i for i in range(N)]
ans = 0
for turn in range(1, K + 1):
    a, b = map(int, input().split())
    union(a, b)
    if ans:
        break
print(ans)