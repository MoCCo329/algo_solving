# 12100. 2048(Easy)  2022-07-26


def dfs(k, arr, path):
    global ans, ans_path
    if k == 5:
        for i in range(N):
            for j in range(N):
                ans = max(ans, int(arr[i][j]))
        return

    for d in ['U', 'D', 'L', 'R']:
        temp_arr = []
        for l in range(N):
            temp = []
            before = '0'
            for m in range(N):
                if d == 'U':
                    i = m
                    j = l
                elif d == 'D':
                    i = N - 1 - m
                    j = l
                elif d == 'L':
                    i = l
                    j = m
                else:
                    i = l
                    j = N - 1 - m

                if arr[i][j] == '0':
                    continue
                elif arr[i][j] == before:
                    temp.append(str(int(before) * 2))
                    before = '0'
                else:
                    if before != '0':
                        temp.append(before)
                    before = arr[i][j]

            if before != '0':
                temp.append(before)

            temp = temp + ['0'] * (N - len(temp))
            if d == 'D' or d == 'R':
                temp = temp[::-1]

            temp_arr.append(temp)

        if d == 'U' or d == 'D':
            temp_arr = [[temp_arr[i][j] for i in range(N)] for j in range(N)]

        dfs(k + 1, temp_arr, path + d)


N = int(input())
arr = [list(input().split()) for _ in range(N)]

ans = 0
dfs(0, arr, '')
print(ans)