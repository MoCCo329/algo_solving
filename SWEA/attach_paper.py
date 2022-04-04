def attach(n):
    a = [1, 3]

    for i in range(2, n//10 + 1):
        a.append(a[i-2] * 2 + a[i-1])

    return a[n//10 - 1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    print(f'#{tc} {attach(N)}')