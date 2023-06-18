# 5676. 음주 코딩  2023-06-18


import sys
input = sys.stdin.readline


def update_query(idx, v):
    idx += 1
    while idx < N + 1:
        fwt[idx] += v
        idx += idx & -idx


def update_zero_query(idx, v):
    idx += 1
    while idx < N + 1:
        zero_fwt[idx] += v
        idx += idx & -idx


def get_query(idx):
    idx += 1
    temp = 0
    while 0 < idx:
        temp += fwt[idx]
        idx &= idx - 1
    return temp


def get_zero_query(idx):
    idx += 1
    temp = 0
    while 0 < idx:
        temp += zero_fwt[idx]
        idx &= idx - 1
    return temp


while True:
    temp = input()
    if len(temp) <= 1:
        break
    N, K = map(int, temp.split())
    arr = list(map(int, input().split()))
    fwt = [0] * (N + 1)
    zero_fwt = [0] * (N + 1)

    for i in range(N):
        if arr[i] < 0:
            update_query(i, 1)
        elif arr[i] == 0:
            update_zero_query(i, 1)

    ans = []
    for i in range(K):
        order, a, b = input().split()
        if order == 'C':
            idx, v = int(a) - 1, int(b)
            if arr[idx] <= 0 and 0 < v:
                if arr[idx] == 0:
                    update_zero_query(idx, -1)
                else:
                    update_query(idx, -1)
                arr[idx] = 1
            elif 0 <= arr[idx] and v < 0:
                if arr[idx] == 0:
                    update_zero_query(idx, -1)
                else:
                    update_query(idx, 1)
                arr[idx] = -1
            elif v == 0:
                if arr[idx] < 0:
                    update_query(idx, -1)
                if arr[idx] != 0:
                    update_zero_query(idx, 1)
                arr[idx] = 0
        else:
            a, b = int(a) - 2, int(b) - 1
            t1, t2 = get_zero_query(a), get_zero_query(b)
            if t2 - t1 > 0:
                ans.append("0")
                continue
            t1, t2 = get_query(a), get_query(b)
            if (t2 - t1) % 2 == 1:
                ans.append("-")
            else:
                ans.append("+")

    print("".join(ans))