for tc in range(1, 11):
    T = int(input())
    Q = list(map(int, input().split()))
    cnt = 0

    while True:
        for j in range(1, 6):
            Q_temp = Q.pop(0)
            if Q_temp > (j):
                Q.append(Q_temp - (j))
            else:
                Q.append(0)
                cnt = 1
                break
        if cnt:
            break

    print(f'#{tc}', *Q)
#
#
#
#
# for tc in range(1, 11):
#     T = int(input())
#     Q = list(map(int, input().split()))
#     cnt = 0
#
#     while 1:
#         for