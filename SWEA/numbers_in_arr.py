d_list = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def dfs(i, j, cnt, word):
    if cnt == 7:
        ans_set.add(word)
        return
    else:
        cnt += 1
        for di, dj in d_list:
            ni, nj = i + di, j + dj
            if 0 <= ni < 4 and 0 <= nj < 4:
                dfs(ni, nj, cnt, word + arr[ni][nj])

T = int(input())
for tc in range(1, T+1):
    arr = [list(map(str, input().split())) for _ in range(4)]
    ans_set = set()

    for i in range(4):
        for j in range(4):
            dfs(i, j, 1, arr[i][j])

    print(f'#{tc} {len(ans_set)}')