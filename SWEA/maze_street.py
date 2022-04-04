# 시작 위치 찾기
def start():
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                return (i, j)

# bfs
def bfs(i, j):
    q = []
    v = [[0] * N for _ in range(N)]
    q.append((i, j))
    v[i][j] = 1

    while q:
        i, j = q.pop(0)
        if arr[i][j] == 3: # 출구를 찾으면 v값 리턴
            return v[i][j] - 2 # 출발칸과 출구칸이 포함되었으므로 -2
        for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] != 1 and v[ni][nj] == 0:
                q.append((ni, nj))
                v[ni][nj] = v[i][j] + 1
    return 0 # 못찾고 while 문이 끝난 경우 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    print(f'#{tc} {bfs(*start())}')