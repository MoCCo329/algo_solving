# 2166. 다각형의 면적  2022-07-27


N = int(input())
points = [list(map(int, input().split())) for _ in range(N)]
points.append(points[0])

ans = 0
for i in range(N):
    ans += points[i][0] * points[i + 1][1]
    ans -= points[i][1] * points[i + 1][0]

print(round(abs(ans) / 2, 2))