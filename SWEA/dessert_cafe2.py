d_list = [[1, 1], [1, -1], [-1, -1], [-1, 1]]

def find(i, j, d, s):
    global ans
    # 도착한 경우
    if d == 3 and (i, j) == origin:
        ans += [len(s)]
        return

    # 도착 안한경우
    if arr[i][j] in s:
        return
    else:
        s += [arr[i][j]]
        ni, nj = i + d_list[d][0], j + d_list[d][1]
        if 0 <= ni < N and 0 <= nj < N:
            find(ni, nj, d, s[:])
        if d < 3:
            ni, nj = i + d_list[d+1][0], j + d_list[d+1][1]
            if 0 <= ni < N and 0 <= nj < N:
                find(ni, nj, d + 1, s[:])
        return

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = []

    for i in range(N-2):
        for j in range(1, N-1):
            s = []
            origin = (i, j)
            find(i, j, 0, s)

    if ans:
        print(f'#{tc} {max(ans)}')
    else:
        print(f'#{tc} -1')