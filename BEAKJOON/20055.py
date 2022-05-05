# 20055 컨베이어 벨트 위의 로봇 G5 2022-05-05


N, K = map(int, input().split())
arr = list(map(int, input().split()))  # 내구도
v = [0] * (2 * N)  # 로봇 여부
up = 0
down = N - 1

ans = 1
while True:
    up = (up - 1) % (2 * N)
    down = (down - 1) % (2 * N)
    if v[down]:
        v[down] = 0

    minIdx = 0
    for i in range(1, 2 * N):
        if v[i] != 0 and v[minIdx] > v[i]:
            minIdx = i
    turn = 2 * N if v[(minIdx + 1) % (2 * N)] else 2 * N - 1
    for _ in range(turn):
        if v[minIdx]:
            next = (minIdx + 1) % (2 * N)
            if v[next] == 0 and arr[next] > 0:
                if next != down:
                    v[next] = v[minIdx]
                v[minIdx] = 0
                arr[next] -= 1
        minIdx = (minIdx - 1) % (2 * N)

    if v[up] == 0 and arr[up] > 0:
        v[up] = ans
        arr[up] -= 1

    cnt = 0
    for i in range(2 * N):
        if arr[i] == 0:
            cnt += 1
    if cnt >= K:
        break

    ans += 1

print(ans)