# 2357. 최솟값과 최댓값  2023-02-07


N, M = map(int, input().split())
k = 1
while k < N: k <<= 1
min_tree = [1000000000] * (k << 1)
max_tree = [1] * (k << 1)
for i in range(N):
    temp = int(input())
    min_tree[i + k] = temp
    max_tree[i + k] = temp

for i in range(k - 1, 0, -1):
    min_tree[i] = min(min_tree[i * 2], min_tree[i * 2 + 1])
    max_tree[i] = max(max_tree[i * 2], max_tree[i * 2 + 1])

for _ in range(M):
    s, e = map(int, input().split())
    s += k - 1
    e += k - 1

    min_n = 1000000000
    max_n = 1
    while s <= e:
        if s % 2 == 1:
            min_n = min(min_n, min_tree[s])
            max_n = max(max_n, max_tree[s])
        if e % 2 == 0:
            min_n = min(min_n, min_tree[e])
            max_n = max(max_n, max_tree[e])

        s = (s + 1) // 2
        e = (e - 1) // 2

    print(min_n, max_n)