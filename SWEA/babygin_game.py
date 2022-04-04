T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))

    tr = [1, 1]
    ru = [1, 1]
    ans = 0
    for i in range(3, 7):
        A = sorted(arr[0:i*2:2])
        B = sorted(arr[1:i*2:2])

        for j in range(1, i):
            if A[j] - A[j-1] == 1:
                tr[0] += 1
            elif A[j - 1] == A[j]:
                ru[0] += 1
            else:
                tr[0] = 1
                ru[0] = 1
            if tr[0] == 3 or ru[0] == 3:
                ans = 1
                break

            if B[j] - B[j - 1] == 1:
                tr[1] += 1
            elif B[j - 1] == B[j]:
                ru[1] += 1
            else:
                tr[1] = 1
                ru[1] = 1
            if tr[1] == 3 or ru[1] == 3:
                ans = 2
                break

        if ans:
            break
    if ans:
        print(f'#{tc} {ans}')
    else:
        print(f'#{tc} 0')