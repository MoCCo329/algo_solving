# 1766. 문제집  2022-07-22


N, M = map(int, input().split())
arr = [[] for _ in range(N + 1)]
ind = [0] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    ind[b] += 1

v = [0] * (N + 1)
ans = []

while True:
    for i in range(1, N + 1):
        if ind[i] == 0 and v[i] == 0:
            break
    else:
        break

    for j in arr[i]:
        ind[j] -= 1
    ans.append(i)
    v[i] = 1

print(*ans)