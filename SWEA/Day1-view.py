for T in range(10):
    N = int(input())
    field = list(map(int, input().split()))

    cnt = 0
    for i in range(N-4):
        for j in range(field[i+2], 0, -1):
            if field[i] < j and field[i+1] < j and field[i+3] < j and field[i+4] < j:
                cnt += 1
            else:
                break

    print(f'#{T+1} {cnt}')