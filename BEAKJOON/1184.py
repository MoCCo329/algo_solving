# 1184. 귀농  2023-05-29


N = int(input())
maps = [list(map(int, input().split())) for _ in range(N)]
sum_maps1 = [[0] * (N + 1) for _ in range(N + 1)]
sum_maps2 = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        sum_maps1[i][j] = sum_maps1[i - 1][j] + sum_maps1[i][j - 1] - sum_maps1[i - 1][j - 1] + maps[i - 1][j - 1]
        sum_maps2[i][j] = sum_maps2[i - 1][j] + sum_maps2[i][j - 1] - sum_maps2[i - 1][j - 1] + maps[i - 1][N - j]

ans = 0
for i in range(1, N):
    for j in range(1, N):
        temp1 = {}
        temp2 = {}
        for k in range(1, i + 1):
            for l in range(1, j + 1):
                temp = sum_maps1[i][j] - sum_maps1[i - k][j] - sum_maps1[i][j - l] + sum_maps1[i - k][j - l]
                if temp1.get(temp, 0) == 0:
                    temp1[temp] = 1
                else:
                    temp1[temp] += 1
                temp = sum_maps2[i][j] - sum_maps2[i - k][j] - sum_maps2[i][j - l] + sum_maps2[i - k][j - l]
                if temp2.get(temp, 0) == 0:
                    temp2[temp] = 1
                else:
                    temp2[temp] += 1
        for k in range(1, N - i + 1):
            for l in range(1, N - j + 1):
                temp = sum_maps1[i + k][j + l] - sum_maps1[i + k][j] - sum_maps1[i][j + l] + sum_maps1[i][j]
                if temp in temp1:
                    ans += temp1[temp]
                temp = sum_maps2[i + k][j + l] - sum_maps2[i + k][j] - sum_maps2[i][j + l] + sum_maps2[i][j]
                if temp in temp2:
                    ans += temp2[temp]

print(ans)