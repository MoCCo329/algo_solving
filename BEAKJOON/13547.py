# 13547. 수열과 쿼리 5  2023-06-13


import sys
input = sys.stdin.readline


N = int(input())
k = int(N ** 0.5)
arr = [0]
arr.extend(map(int, input().split()))

M = int(input())
queries = []
for i in range(M):
    queries.append([*map(int, input().split()), i])
queries.sort(key=lambda x: (x[0] // k, x[1], x[0]))  # or x[1] // k

ans = [0] * M
counts = [0] * 1000001
before = 0
for i in range(queries[0][0], queries[0][1] + 1):
    counts[arr[i]] += 1
    if counts[arr[i]] == 1:
        before += 1
ans[queries[0][2]] = before

for i in range(1, M):
    if queries[i][0] < queries[i - 1][0]:
        for j in range(queries[i][0], queries[i - 1][0]):
            counts[arr[j]] += 1
            if counts[arr[j]] == 1:
                before += 1
    else:
        for j in range(queries[i - 1][0], queries[i][0]):
            counts[arr[j]] -= 1
            if counts[arr[j]] == 0:
                before -= 1
    if queries[i][1] < queries[i - 1][1]:
        for j in range(queries[i - 1][1], queries[i][1], -1):
            counts[arr[j]] -= 1
            if counts[arr[j]] == 0:
                before -= 1
    else:
        for j in range(queries[i - 1][1] + 1, queries[i][1] + 1):
            counts[arr[j]] += 1
            if counts[arr[j]] == 1:
                before += 1

    ans[queries[i][2]] = before

for n in ans:
    print(n, sep="\n")