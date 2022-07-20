# 4386. 별자리 만들기  2022-07-20


N = int(input())
arr = [[0] * (N + 1) for _ in range(N + 1)]
stars = [list(map(float, input().split())) for _ in range(N)]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i >= j:
            continue

        temp = ((stars[i - 1][0] - stars[j - 1][0]) ** 2 + (stars[i - 1][1] - stars[j - 1][1]) ** 2) ** 0.5
        arr[i][j] = temp
        arr[j][i] = temp

D = [1500] * (N + 1)
D[1] = 0
V = [0] * (N + 1)
ans = 0

for _ in range(N + 1):

    min_idx = 0
    min_D = 1500
    for i in range(1, N + 1):
        if min_D > D[i] and V[i] == 0:
            min_idx = i
            min_D = D[i]
    if min_idx == 0:
        break
    ans += min_D
    V[min_idx] = 1

    for i in range(1, N + 1):
        if arr[min_idx][i] != 0:
            D[i] = min(D[i], arr[min_idx][i])

# print("%.2f" % (ans))
# print("{:.2f}".format(ans))
print(f"{ans:.2f}")