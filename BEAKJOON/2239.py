# 2239. 스도쿠  2022-07-24


def dfs(k):
    if k == 81:
        for i in range(9):
            print(''.join(map(str, arr[i])))
        exit(0)

    i = k // 9
    j = k % 9

    if arr[i][j]:
        dfs(k + 1)
        return

    l, m = i // 3, j // 3
    counts = [0] * 10
    for idx in range(9):
        counts[arr[idx][j]] += 1
        counts[arr[i][idx]] += 1
    for ii in range(3):
        for jj in range(3):
            counts[arr[3 * l + ii][3 * m + jj]] += 1

    for num in range(1, 10):
        if counts[num] == 0:
            arr[i][j] = num
            dfs(k + 1)
            arr[i][j] = 0


arr = [list(map(int, input())) for _ in range(9)]
dfs(0)