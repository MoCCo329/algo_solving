# 15685. 드래곤 커브 2022-04-17


d_list = [[0, 1], [-1, 0], [0, -1], [1, 0]]

N = int(input())
arr = [[0] * 101 for _ in range(101)]

for _ in range(N):
    j, i, d, g = map(int, input().split())

    q = [d]
    arr[i][j] = 1
    for _ in range(g + 1):
        L = len(q)
        for k in range(L // 2, L):
            di, dj = d_list[q[k]]
            i, j = i + di, j + dj
            arr[i][j] = 1
        q = q + [(q[i] + 1) % 4 for i in range(L - 1, -1, -1)]

ans = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] == 1 and arr[i + 1][j] == 1 and arr[i][j + 1] == 1 and arr[i + 1][j + 1] == 1:
            ans += 1

print(ans)