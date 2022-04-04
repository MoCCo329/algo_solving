def bfs(i, j):
    v = [[0]*16 for _ in range(16)]
    q = []
    q.append((i, j))
    v[i][j] = 1
    while q:
        i, j = q.pop(0)
        if arr[i][j] == 3:
            return 1
        for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            ni, nj = i+di, j+dj
            if arr[ni][nj] != 1 and v[ni][nj] == 0:
                q.append((ni, nj))
                v[ni][nj] = 1
    return 0

def find_start():
    for i in range(16):
        for j in range(16):
            if arr[i][j] == 2:
                return (i, j)

for _ in range(1, 11):
    T = int(input())
    arr = [list(map(int, input())) for _ in range(16)]

    i, j = find_start()
    print(f'#{T} {bfs(i, j)}')