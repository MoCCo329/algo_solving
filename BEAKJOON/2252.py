# 2252. 줄 세우기  2022-07-26


N, M = map(int, input().split())
adj_list = [[] for _ in range(N + 1)]
ind = [0] * (N + 1)
v = [0] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    adj_list[a].append(b)
    ind[b] += 1

while True:
    for i in range(1, N + 1):
        if ind[i] == 0 and v[i] == 0:
            print(i, end=' ')
            for j in adj_list[i]:
                ind[j] -= 1
            v[i] = 1
            break
    else:
        break