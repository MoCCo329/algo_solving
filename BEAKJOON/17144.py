# 17144. 미세먼지 안녕! 2022-04-26


def spread(i, j):
    spreadD = arr[i][j] // 5
    for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        ni, nj = i + di, j + dj
        if 0 <= ni < N and 0 <= nj < M and (ni, nj) not in [(airTop, 0), (airBottom, 0)]:
            newArr[ni][nj] += spreadD
            newArr[i][j] -= spreadD


N, M, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    if arr[i][0] == -1:
        airTop = i
        airBottom = i + 1
        arr[i][0] = 0
        arr[i + 1][0] = 0
        break

for _ in range(T):
    # 확산
    newArr = [arr[i][::] for i in range(N)]
    for i in range(N):
        for j in range(M):
            if arr[i][j]:
                spread(i, j)

    # 순환 및 arr에 복사
    for i in range(airTop):
        arr[i + 1][0] = newArr[i][0]
        arr[i][-1] = newArr[i + 1][-1]

    for i in range(airBottom, N - 1):
        arr[i][0] = newArr[i + 1][0]
        arr[i + 1][-1] = newArr[i][-1]
    arr[0] = newArr[0][1:][::] + [newArr[1][-1]]
    arr[airTop] = [0, 0] + newArr[airTop][1:M - 1][::]
    arr[airBottom] = [0, 0] + newArr[airBottom][1:M - 1][::]
    arr[N - 1] = newArr[N - 1][1:][::] + [newArr[N - 2][-1]]

    for i in range(1, N - 1):
        if i != airTop and i != airBottom:
            arr[i][1:M - 1] = newArr[i][1:M - 1][::]

ans = 0
for i in range(N):
    for j in range(M):
        ans += arr[i][j]
print(ans)