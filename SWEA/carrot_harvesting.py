T  = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    first = 0
    second = 0
    for carrot in arr:
        second += carrot

    gap = second
    while first >= 0 and second > 0:
        for i in range(N):
            first += arr[i]
            second -= arr[i]
            if gap > abs(second - first):
                gap = abs(second - first)
                answer = [i+1, gap]
    print(f'#{tc}', *answer)