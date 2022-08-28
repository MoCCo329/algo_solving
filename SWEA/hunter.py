# 문제번호 X


def find(i, K):
    global new_order, orders

    if i == K:
        vv = [0] * (K // 2 + 1)
        for j in range(K):
            temp = new_order[j]
            if temp < 0:
                if not vv[-temp]:
                    break
            else:
                vv[temp] = 1
        else:
            orders.append(new_order[::])

    else:
        for j in range(K):
            if v[j] == 0:
                v[j] = 1
                new_order[i] = order[j]
                find(i + 1, K)
                v[j] = 0


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    client = [0] * 5
    monster = [0] * 5
    order = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] > 0:
                monster[arr[i][j]] = (i, j)
                order.append(arr[i][j])
            elif arr[i][j] < 0:
                client[-arr[i][j]] = (i, j)
                order.append(arr[i][j])

    K = len(order)
    new_order = [0] * K
    orders = []
    v = [0] * K
    find(0, K)

    ans = 4 * N * K
    while orders:
        temp_ans = 0
        i, j = 0, 0
        test_order = orders.pop()

        for num in test_order:
            if num < 0:
                ni, nj = client[-num]
            else:
                ni, nj = monster[num]
            temp_ans += abs(ni - i) + abs(nj - j)
            i, j = ni, nj

        if temp_ans < ans:
            ans = temp_ans

    print(f'#{tc} {ans}')