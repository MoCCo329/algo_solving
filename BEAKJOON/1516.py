# 1516. 게임 개발  2023-06-25


from collections import deque


N = int(input())
adj_list = [[] for _ in range(N + 1)]
incomes = [0] * (N + 1)
times = [0] * (N + 1)
build_t = [0] * (N + 1)
for i in range(1, N + 1):
    t, *nums = map(int, input().split())
    times[i] = t
    for j in nums[:-1]:
        adj_list[j].append(i)
        incomes[i] += 1

q = deque()
for i in range(1, N + 1):
    if incomes[i] == 0:
        build_t[i] = times[i]
        q.append(i)

while q:
    i = q.popleft()
    for j in adj_list[i]:
        incomes[j] -= 1
        build_t[j] = max(build_t[j], build_t[i] + times[j])
        if incomes[j] == 0:
            q.append(j)

for i in range(1, N + 1):
    print(build_t[i])