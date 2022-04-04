T = int(input())
for tc in range(1,T+1):
    arr = list(map(int, input().split()))
    cnt=0

    for i in range(1, 1<<10):
        sum = 0
        for j in range(10):
            if i & (1<<j):
                sum += arr[j]
        if sum == 0 :
            cnt += 1
            break
    if cnt != 0:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')