# 1976. 여행가자  2022-07-18


N = int(input())
M = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
M_list = list(map(lambda x: int(x) - 1, input().split()))

for i in range(N):
    for j in range(N):
        if i != j and arr[i][j] == 0:
            arr[i][j] = -1

for k in range(N):
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if arr[i][k] != -1 and arr[k][j] != -1 and (arr[i][j] == -1 or arr[i][j] > arr[i][k] + arr[k][j]):
                arr[i][j] = arr[i][k] + arr[k][j]
                arr[j][i] = arr[i][k] + arr[k][j]

for i in range(1, M):
    if arr[M_list[i - 1]][M_list[i]] == -1:
        print("NO")
        break
else:
    print("YES")