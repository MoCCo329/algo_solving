# 17371. 이사  2023-01-28


def cal_dist(i1, j1, i2, j2):
    return (i1 - i2) ** 2 + (j1 - j2) ** 2


N = int(input())
facility = [tuple(map(int, input().split())) for _ in range(N)]

ans = 0
min_dia = 10 ** 9
for i in range(N):
    max_dist = 0

    for j in range(N):
        if i == j: continue

        max_dist = max(max_dist, cal_dist(*facility[i], *facility[j]))

    if max_dist < min_dia:
        min_dia = max_dist
        ans = i

print(facility[ans][0], facility[ans][1])