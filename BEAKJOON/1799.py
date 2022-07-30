# 1799. 비숍  2022-07-29


# 시간초과

def dfs(type, k, end, cnt):
    global ans_b, ans_w

    if k == end:
        if type == 'black':
            ans_b = max(ans_b, cnt)
        else:
            ans_w = max(ans_w, cnt)
        return

    for i in range(k, end):
        if type=='black':
            temp = black
        else:
            temp = white
        if not v[temp[i][0]] and not v[temp[i][1]]:
            v[temp[i][0]] = 1
            v[temp[i][1]] = 1
            dfs(type, i + 1, end, cnt + 1)
            v[temp[i][0]] = 0
            v[temp[i][1]] = 0


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
v = [0] * (4 * N - 2)

black = []
white = []
for i in range(N):
    for j in range(N):
        if arr[i][j]:
            if (i + j) % 2:
                black.append((i + j, - j + i + 3 * N - 2))
            else:
                white.append((i + j, - j + i + 3 * N - 2))

ans_b, ans_w = 0, 0
if black:
    dfs('black', 0, len(black), 0)
if white:
    dfs('white', 0, len(white), 0)
print(ans_b + ans_w)