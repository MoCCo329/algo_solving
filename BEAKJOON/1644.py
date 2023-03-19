# 1644. 소수의 연속합  2023-03-19


import math


N = int(input())
arr = [1] * (N + 1)
for i in range(2, int(math.sqrt(N)) + 1):
    if arr[i] == 0: continue

    for j in range(i * 2, N + 1, i):
        arr[j] = 0

i = 2
j = 2
now = 2
ans = 0

while i <= j <= N:
    if now < N:
        j += 1
        while j <= N and arr[j] == 0:
            j += 1
        now += j
    if now >= N:
        if now == N:
            ans += 1
        now -= i
        i += 1
        while i <= N and arr[i] == 0:
            i += 1

print(ans)