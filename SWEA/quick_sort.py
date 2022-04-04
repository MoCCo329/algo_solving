def partition(a, b, e):
    pivot = (b + e) // 2
    L = b
    R = e

    while L < R:
        while L < R and a[L] < a[pivot]:
            L += 1
        while L < R and a[R] >= a[pivot]:
            R -= 1
        if L < R:
            if L == pivot:
                pivot = R
            a[L], a[R] = a[R], a[L]
    a[pivot], a[R] = a[R], a[pivot]
    return R


def partition2(a, b, e):
    pivot = b
    L = b
    R = e
    while L < R:
        while L <= R and a[L] <= a[pivot]:
            L += 1
        while L <= R and a[R] >= a[pivot]:
            R -= 1
        if L < R:
            a[L], a[R] = a[R], a[L]
    a[pivot], a[R] = a[R], a[pivot]
    return R


def quick_sort(a, b, e):
    if b < e:
        p = partition2(a, b, e)
        quick_sort(a, b, p-1)   # 파티션 좌측
        quick_sort(a, p+1, e)   # 파티션 우측


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    a = list(map(int,input().split()))
    quick_sort(a, 0, N-1)
    print(f'#{tc}', a[N//2])