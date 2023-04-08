# 1153. 네 개의 소수  2023-04-09


import math


def DFS(cnt, k):
    tot = sum(ans_arr)
    if cnt == 2:
        if tot == N:
            print(*sorted(ans_arr))
            exit(0)
        return

    if tot >= N:
        return

    for i in range(k, len(prime_arr)):
        ans_arr[cnt] = prime_arr[i]
        DFS(cnt + 1, i)
        ans_arr[cnt] = 0


N = int(input())
ans_arr = [0, 0, 2, 2]
if N < 8:
    print(-1)
    exit(0)
if N % 2 == 1:
    ans_arr[3] = 3

arr = [1] * N
arr[0], arr[1] = 0, 0
prime_arr = []

for i in range(2, int(math.sqrt(N)) + 1):
    if arr[i] == 0: continue

    temp = i * 2
    while temp < N:
        arr[temp] = 0
        temp += i

for i in range(2, N):
    if arr[i] == 1:
        prime_arr.append(i)

DFS(0, 0)
print(-1)