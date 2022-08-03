# 12852. 1로 만들기 2  2022-08-03


N = int(input())
arr = [0 for _ in range(N + 1)]
arr[1] = (0, 0)

for i in range(1, N + 1):
    if arr[i]:
        cnt, before = arr[i]
        if i + 1 <= N and (arr[i + 1] == 0 or arr[i + 1][0] > cnt + 1):
            arr[i + 1] = (cnt + 1, i)
        if i * 2 <= N and (arr[i * 2] == 0 or arr[i * 2][0] > cnt):
            arr[i * 2] = (cnt + 1, i)
        if i * 3 <= N and (arr[i * 3] == 0 or arr[i * 3][0] > cnt):
            arr[i * 3] = (cnt + 1, i)

if N == 1:
    print(0)
    print(1)
else:
    path = [N]
    i = N
    while arr[i][1] != 0:
        path.append(arr[i][1])
        i = arr[i][1]

    print(len(path) - 1)
    print(*path)