# 4311. 오래된 스마트폰 2022-06-02


T = int(input())
for tc in range(1, T + 1):
    N, O, M = map(int, input().split())
    nums = list(map(int, input().split()))
    oper = list(map(int, input().split()))
    W = int(input())

    arr = [[0] * 1000 for _ in range(M)]
    for ex in range(3):
        for i in range(10 ** ex):
            for n in nums:
                arr[ex][int(str(i) + str(n))] = 1

    for i in range()