# 2632. 피자판매 2022-07-14


def bs(arr, val):
    L = 0
    R = len(arr) - 1
    v1, v2 = len(arr), len(arr)
    while L <= R:
        M = (L + R) // 2
        if arr[M] >= val:
            R = M - 1
            v1 = min(v1, M)
        else:
            L = M + 1

    R = len(arr) - 1
    while L <= R:
        M = (L + R) // 2
        if arr[M] > val:
            R = M - 1
            v2 = min(v2, M)
        else:
            L = M + 1

    return v2 - v1


K = int(input())
N, M = map(int, input().split())
A = [int(input()) for _ in range(N)]
B = [int(input()) for _ in range(M)]

arr_A = [0, sum(A)]
arr_B = [0, sum(B)]

for k in range(1, N):
    temp = sum(A[:k])
    arr_A.append(temp)
    i = 0
    for i in range(N - 1):
        temp += -A[i] + A[(i + k) % N]
        arr_A.append(temp)
        i += 1
for k in range(1, M):
    temp = sum(B[:k])
    arr_B.append(temp)
    i = 0
    for i in range(M - 1):
        temp += -B[i] + B[(i + k) % M]
        arr_B.append(temp)
        i += 1

arr_A.sort()
arr_B.sort()

ans = 0
for a in range(K + 1):
    b = K - a
    ans += bs(arr_A, a) * bs(arr_B, b)
print(ans)