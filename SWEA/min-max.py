for T in range(int(input())):
    N = int(input())
    arr = list(map(int, input().split()))
    maxV = arr[0]
    minV = arr[0]

    for i in range(1, N):
        if arr[i] >= maxV:
            maxV = arr[i]
        if arr[i] <= minV:
            minV = arr[i]

    print(f'#{T+1} {maxV-minV}')