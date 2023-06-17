# 13548. 수열과 쿼리 6  2023-06-17


import sys
input = sys.stdin.readline


def update(n, v):
    global max_v

    if v > 0:
        c_counts[counts[n]] -= 1
        counts[n] += 1
        c_counts[counts[n]] += 1
        max_v = max(max_v, counts[n])
    else:
        if counts[n] == max_v and c_counts[counts[n]] == 1:
            max_v -= 1
        c_counts[counts[n]] -= 1
        counts[n] -= 1
        c_counts[counts[n]] += 1


N = int(input())
arr = list(map(int, input().split()))
M = int(input())
querys = []
for i in range(M):
    a, b = map(int, input().split())
    querys.append((a - 1, b - 1, i))
k = int(N ** 0.5)
querys.sort(key=lambda x: (x[0] // k, x[1], x[0]))

ans = [0] * M
counts = [0] * 100001
c_counts = [0] * 100001

arr_i = -1
arr_j = 0
max_v = 0
for q_i in range(M):
    while arr_i < querys[q_i][1]:
        arr_i += 1
        update(arr[arr_i], 1)
    while querys[q_i][1] < arr_i:
        update(arr[arr_i], -1)
        arr_i -= 1
    while arr_j < querys[q_i][0]:
        update(arr[arr_j], -1)
        arr_j += 1
    while querys[q_i][0] < arr_j:
        arr_j -= 1
        update(arr[arr_j], 1)

    ans[querys[q_i][2]] = max_v

for i in range(M):
    print(ans[i])